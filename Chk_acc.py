from settrade_v2 import Investor
from settrade_v2.errors import SettradeError
import pandas as pd

investor = Investor(
                app_id="UZt5g6qBPcQy59mR",
                app_secret="TBqZ5hvTkFr01cVkt2h8sRDa7QmKQrFwL19Ox+R61Wk=",
                broker_id="023",
                app_code="ALGO",
                is_auto_queue = False)

deri = investor.Derivatives(account_no="508318-0")
account_info = deri.get_account_info()
trade_list = deri.get_trades()
order_list = deri.get_orders()
