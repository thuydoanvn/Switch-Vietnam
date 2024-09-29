"""
This is a standard Switch module. You can use it in your model by placing it in
the main model directory and then adding `new_transmission_limit` to
modules.txt. This should be somewhere below
switch_model.transmission.transport.build in modules.txt, because it depends on
some components defined there.

See Section 3 of the Switch tutorial
(https://github.com/switch-model/switch_tutorial/raw/master/Switch_Tutorial.pdf)
for more information.

Also see any existing Switch modules (e.g.,
https://github.com/switch-model/switch/blob/master/switch_model/transmission/transport/build.py)
for useful examples and details on existing Params, Vars and Expressions you may
want to reference.

Once this is finished, you should be able to run the model with no
trans_limit_mw_km.csv file or with only dots for the limits, to setup the base
case (with no transmission limit). If you also specify `--save-expression
TxTotalMWkm` on the command line or in options.txt, Switch will report how much
transmission capacity was built in the base case in outputs/TxTotalMWkm.csv.
Then you can use that to fill in trans_limit_mw_km.csv for other scenarios.

"""
from __future__ import division
import os
from pyomo.environ import *

def define_components(m):
    # This function will be called automatically as the model is constructed.
    # It can add anything you want onto the model (m).

    # Make a new param to hold the input data. It has a default value so we can
    # specify "." in the input or omit the input and it will be unlimited.
    m.trans_limit_mw_km = Param(
        m.PERIODS,
        within=NonNegativeReals,
        default=float("inf")
    )

    # Define an expression that calculates the MW-km added in each study period.
    # This can use m.TRANSMISSION_LINES, m.PERIODS, m.trans_length_km and m.BuildTx
    # (switch_model.transmission.transport.build shows how these were defined).
    m.TxTotalMWkm = Expression(
        m.PERIODS,
        rule=lambda m, p: sum(
            m.BuildTx[tx, p] * m.trans_length_km[tx]
            for tx in m.TRANSMISSION_LINES
        ),
    )

    # Define a constraint to ensure m.TxTotalMWkm[p] <= m.trans_limit_mw_km[p]
    # for each period.
    m.Limit_Total_Transmission = Constraint(
        m.PERIODS,
        rule=lambda m, p: (
            m.TxTotalMWkm[p] <= m.trans_limit_mw_km[p]
        ),
    )

    # Note: if you receive errors from the solver when m.trans_limit_mw_km[p] is
    # equal to infinity in the constraint above, you could skip the constraint
    # for all those periods. See Enforce_RFM_Supply_Tier_Activated in
    # switch_model.hawaii.fuel_markets_expansion for an example.


def load_inputs(mod, switch_data, inputs_dir):
    # this function specifies any data that should be read into the model
    """
    Import the cap on MW-km of transmission in each period.

    new_transmission_limit.csv
        PERIOD, trans_limit_mw_km
    """

    # TODO: change statement below (copied from switch_model.transmission.transport.build)
    # to read trans_limit_mw_km from new_transmission_limit.csv
    switch_data.load_aug(
        filename=os.path.join(inputs_dir, "new_transmission_limit.csv"),
        optional=True,
        param=(
            mod.trans_limit_mw_km,
        ),
    )