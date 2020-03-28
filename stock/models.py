from django.db import models

class StockInfo(models.Model):
	pair_ID = models.DecimalField()
	stock_symbol = models.CharField()
	parent_pair_ID = models.BooleanField()
	canonical_to_pair_id = models.BooleanField()
	override_country_ID = models.BooleanField()
	eq_pe_ratio = models.DecimalField(null=True)
	eq_market_cap = models.DecimalField(null=True)
	eq_one_year_return = models.DecimalField(null=True)
	eq_dividend = models.DecimalField(null=True)
	eq_eps = models.DecimalField(null=True)
	eq_beta = models.DecimalField(null=True)
	eq_revenue = models.DecimalField(null=True)
	exchange_ID = models.DecimalField()
	security_type = models.CharField()
	a1fcf = models.DecimalField(null=True)
	aastturn = models.DecimalField(null=True)
	abepsxclxo = models.DecimalField(null=True)
	abvps = models.DecimalField(null=True)
	acfshr = models.DecimalField(null=True)
	acshps = models.DecimalField(null=True)
	acurratio = models.DecimalField(null=True)
	adiv5yavg = models.DecimalField(null=True)
	aebitd = models.DecimalField(null=True)
	aebt = models.DecimalField(null=True)
	aebtnorm = models.DecimalField(null=True)
	aepsinclxo = models.DecimalField(null=True)
	aepsxclxor = models.DecimalField(null=True)
	agrosmgn = models.DecimalField(null=True)
	ainvturn = models.DecimalField(null=True)
	altd2eq = models.DecimalField(null=True)
	aniac = models.DecimalField(null=True)
	aniacnorm = models.DecimalField(null=True)
	anpmgnpct = models.DecimalField(null=True)
	aopmgnpct = models.DecimalField(null=True)
	apayratio = models.DecimalField(null=True)
	apeexclxor = models.DecimalField(null=True)
	apenorm = models.DecimalField(null=True)
	apr2rev = models.DecimalField(null=True)
	apr2tanbk = models.DecimalField(null=True)
	aprfcfps = models.DecimalField(null=True)
	aprice2bk = models.DecimalField(null=True)
	aptmgnpct = models.DecimalField(null=True)
	aquickrati = models.DecimalField(null=True)
	arecturn = models.DecimalField(null=True)
	arevps = models.DecimalField(null=True)
	aroa5yavg = models.DecimalField(null=True)
	aroapct = models.DecimalField(null=True)
	aroe5yavg = models.DecimalField(null=True)
	aroepct = models.DecimalField(null=True)
	aroi5yravg = models.DecimalField(null=True)
	aroipct = models.DecimalField(null=True)
	atanbvps = models.DecimalField(null=True)
	atotd2eq = models.DecimalField(null=True)
	beta = models.DecimalField(null=True)
	bvtrendgr = models.DecimalField(null=True)
	csptrendgr = models.DecimalField(null=True)
	divgrpct = models.DecimalField(null=True)
	divyield_curttm = models.DecimalField(null=True)
	ebitda_ayr5cagr = models.DecimalField(null=True)
	ebitda_ttmy5cagr = models.DecimalField(null=True)
	epschngyr = models.DecimalField(null=True)
	epsgrpct = models.DecimalField(null=True)
	epstrendgr = models.DecimalField(null=True)
	ev2fcf_cura = models.DecimalField(null=True)
	ev2fcf_curttm = models.DecimalField(null=True)
	focf2rev_aavg5 = models.DecimalField(null=True)
	focf2rev_ttm = models.DecimalField(null=True)
	focf_ayr5cagr = models.DecimalField(null=True)
	grosmgn5yr = models.DecimalField(null=True)
	margin5yr = models.DecimalField(null=True)
	mktcap = models.DecimalField(null=True)
	netdebt_a = models.DecimalField(null=True)
	netdebt_i = models.DecimalField(null=True)
	npmtrendgr = models.DecimalField(null=True)
	opmgn5yr = models.DecimalField(null=True)
	pebexclxor = models.DecimalField(null=True)
	peexclxor = models.DecimalField(null=True)
	peinclxor = models.DecimalField(null=True)
	pr2tanbk = models.DecimalField(null=True)
	price2bk = models.DecimalField(null=True)
	projepsq = models.DecimalField(null=True)
	ptmgn5yr = models.DecimalField(null=True)
	qbvps = models.DecimalField(null=True)
	qcshps = models.DecimalField(null=True)
	qcurratio = models.DecimalField(null=True)
	qltd2eq = models.DecimalField(null=True)
	qquickrati = models.DecimalField(null=True)
	qtanbvps = models.DecimalField(null=True)
	qtotd2eq = models.DecimalField(null=True)
	revchngyr = models.DecimalField(null=True)
	revgrpct = models.DecimalField(null=True)
	revps5ygr = models.DecimalField(null=True)
	revtrendgr = models.DecimalField(null=True)
	sharesout = models.DecimalField(null=True)
	stld_ayr5cagr = models.DecimalField(null=True)
	tanbv_ayr5cagr = models.DecimalField(null=True)
	ttmastturn = models.DecimalField(null=True)
	ttmbepsxcl = models.DecimalField(null=True)
	ttmcfshr = models.DecimalField(null=True)
	ttmebitd = models.DecimalField(null=True)
	ttmebitdps = models.DecimalField(null=True)
	ttmebt = models.DecimalField(null=True)
	ttmepschg = models.DecimalField(null=True)
	ttmepsincx = models.DecimalField(null=True)
	ttmepsxclx = models.DecimalField(null=True)
	ttmfcf = models.DecimalField(null=True)
	ttmfcfshr = models.DecimalField(null=True)
	ttmgrosmgn = models.DecimalField(null=True)
	ttminvturn = models.DecimalField(null=True)
	ttmniac = models.DecimalField(null=True)
	ttmnpmgn = models.DecimalField(null=True)
	ttmopmgn = models.DecimalField(null=True)
	ttmpayrat = models.DecimalField(null=True)
	ttmpehigh = models.DecimalField(null=True)
	ttmpelow = models.DecimalField(null=True)
	ttmpr2rev = models.DecimalField(null=True)
	ttmprcfps = models.DecimalField(null=True)
	ttmprfcfps = models.DecimalField(null=True)
	ttmptmgn = models.DecimalField(null=True)
	ttmrecturn = models.DecimalField(null=True)
	ttmrevchg = models.DecimalField(null=True)
	ttmrevps = models.DecimalField(null=True)
	ttmroapct = models.DecimalField(null=True)
	ttmroepct = models.DecimalField(null=True)
	ttmroipct = models.DecimalField(null=True)
	vdes_ttm = models.DecimalField(null=True)
	yld = models.DecimalField(null=True) # check
	yld5yavg = models.DecimalField(null=True)
	RSI = models.DecimalField(null=True)
	STOCH = models.DecimalField(null=True)
	CCI = models.DecimalField(null=True)
	MACD = models.DecimalField(null=True)
	ADX = models.DecimalField(null=True)
	WilliamsR = models.DecimalField(null=True)
	STOCHRSI = models.DecimalField(null=True)
	ATR = models.DecimalField(null=True)
	HL = models.DecimalField(null=True)
	UO = models.DecimalField(null=True)
	ROC = models.DecimalField(null=True)
	BullBear = models.DecimalField(null=True)
	tech_sum_300 = models.CharField(null=True)
	tech_sum_300_Define = models.CharField(null=True)
	tech_sum_300_Define_order_priority = models.DecimalField(null=True)
	tech_sum_300_Color = models.CharField(null=True)
	tech_sum_900 = models.CharField(null=True)
	tech_sum_900_Define = models.CharField(null=True)
	tech_sum_900_Define_order_priority = models.DecimalField(null=True)
	tech_sum_900_Color = models.CharField(null=True)
	tech_sum_1800 = models.CharField(null=True)
	tech_sum_1800_Define = models.CharField(null=True)
	tech_sum_1800_Define_order_priority = models.DecimalField(null=True)
	tech_sum_1800_Color = models.CharField(null=True)
	tech_sum_3600 = models.CharField(null=True)
	tech_sum_3600_Define = models.CharField(null=True)
	tech_sum_3600_Define_order_priority = models.DecimalField(null=True)
	tech_sum_3600_Color = models.CharField(null=True)
	tech_sum_18000 = models.CharField(null=True)
	tech_sum_18000_Define = models.CharField(null=True)
	tech_sum_18000_Define_order_priority = models.DecimalField(null=True)
	tech_sum_18000_Color = models.CharField(null=True)
	tech_sum_86400 = models.CharField(null=True)
	tech_sum_86400_Define = models.CharField(null=True)
	tech_sum_86400_Define_order_priority = models.DecimalField(null=True)
	tech_sum_86400_Color = models.CharField(null=True)
	tech_sum_week = models.CharField(null=True)
	tech_sum_week_Define = models.CharField(null=True)
	tech_sum_week_Define_order_priority = models.DecimalField(null=True)
	tech_sum_week_Color = models.CharField(null=True)
	tech_sum_month = models.CharField(null=True)
	tech_sum_month_Define = models.CharField(null=True)
	tech_sum_month_Define_order_priority = models.DecimalField(null=True)
	tech_sum_month_Color = models.CharField(null=True)
	month_change = models.DecimalField(null=True)
	ytd = models.DecimalField(null=True)
	week = models.DecimalField(null=True)
	month = models.DecimalField(null=True)
	year = models.DecimalField(null=True)
	year3 = models.DecimalField(null=True) # check
	sector_id = models.DecimalField(null=True)
	industry_id = models.DecimalField(null=True)
	avg_volume = models.DecimalField()
	pair_change_percent = models.DecimalField()
	a52_week_high = models.DecimalField()
	a52_week_low = models.DecimalField()
	turnover_volume = models.DecimalField()
	last = models.DecimalField()
	a52_week_high_diff = models.DecimalField()
	a52_week_low_diff = models.DecimalField()
	exchange_trans = models.CharField()
	name_trans = models.CharField()
	sector_trans = models.CharField(null=True)
	industry_trans = models.CharField(null=True)
	viewData = models.CharField()
	tech_sum_300_constant = models.CharField(null=True)
	tech_sum_900_constant = models.CharField(null=True)
	tech_sum_1800_constant = models.CharField(null=True)
	tech_sum_3600_constant = models.CharField(null=True)
	tech_sum_18000_constant = models.CharField(null=True)
	tech_sum_86400_constant = models.CharField(null=True)
	tech_sum_week_constant = models.CharField(null=True)
	tech_sum_month_constant = models.CharField(null=True)
	daily = models.DecimalField()
	current_assets = models.DecimalField(null=True)
	assets = models.DecimalField(null=True)
	current_liabilities = models.DecimalField(null=True)
	liabilities = models.DecimalField(null=True)
	capital = models.DecimalField(null=True)
	aintcov = models.DecimalField(null=True)
	ttmintcov = models.DecimalField(null=True)
	aniperemp = models.DecimalField(null=True)
	arevperemp = models.DecimalField(null=True)
	ttmniperem = models.DecimalField(null=True)
	ttmrevpere = models.DecimalField(null=True)
