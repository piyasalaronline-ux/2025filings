import yfinance as yf
import json
import os
import time

DATA_FOLDER = 'USDATAyfinance'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# NASDAQ 100 Listesi (Listenin tamamı)
tickers = [
    "AAL","AAON","AAPL","ABNB","ACAD","ACGL","ACGLN","ACGLO","ACIW","ACLS","ACLX","ACT","ADAMI","ADAML","ADAMM","ADAMN","ADBE","ADI","ADP","ADPT","ADSK","ADUS","AEIS","AEP","AFRM","AGIO","AGNC","AGNCL","AGNCM","AGNCN","AGNCO","AGNCP","AGNCZ","AGYS","AKAM","AKRO","ALAB","ALGM","ALGN","ALHC","ALKS","ALKT","ALNY","ALRM","AMAT","AMBA","AMD","AMGN","AMKR","AMRX","AMZN","APA","APLD","APLS","APP","ARCC","ARGX","ARLP","ARM","ARQT","ARWR","ASML","ASND","ASO","ASTS","ATAT","ATEC","AUGO","AUR","AVAV","AVGO","AVPT","AVT","AXON","AZN","BANF","BANR","BATRA","BATRK","BBIO","BCPC","BEAM","BGC","BHF","BIDU","BIIB","BILI","BKNG","BKR","BL","BLKB","BLLN","BMRN","BNTX","BOKF","BPOP","BPYPM","BPYPN","BPYPO","BPYPP","BRKR","BRKRP","BRZE","BSY","BTSG","BTSGU","BUSE","BUSEP","BWIN","BZ","CACC","CAI","CAKE","CALM","CAR","CARG","CART","CASY","CATY","CBSH","CCC","CCEP","CDNS","CDW","CEG","CENX","CFLT","CG","CGABL","CGNX","CGON","CHDN","CHEF","CHKP","CHRD","CHRW","CHTR","CHYM","CIFR","CIGI","CINF","CLBT","CMCSA","CME","CNTA","CNXC","COCO","COGT","COIN","COKE","COLB","COLM","COMM","COO","CORZ","CORZW","CORZZ","COST","CPB","CPRT","CRDO","CRNX","CROX","CRUS","CRVL","CRWD","CRWV","CSCO","CSGP","CSGS","CSIQ","CSQ","CSX","CTAS","CTSH","CVBF","CVCO","CVLT","CWST","CYBR","CYTK","CZR","DASH","DBX","DDOG","DHCNI","DHCNL","DIOD","DKNG","DLO","DLTR","DNLI","DOCU","DOOO","DORM","DOX","DPZ","DRS","DRVN","DSGX","DUOL","DXCM","DYN","EA","EBAY","EBC","EEFT","ENLT","ENSG","ENTG","EQIX","ERIC","ERIE","ESLT","ETOR","EVRG","EWBC","EWTX","EXC","EXE","EXEEL","EXEL","EXLS","EXPE","EXPO","EXTR","FA","FANG","FAST","FBNC","FCFS","FCNCA","FELE","FER","FFBC","FFIN","FFIV","FHB","FIBK","FIGR","FISV","FITB","FITBI","FITBO","FITBP","FIVE","FIZZ","FLEX","FLNC","FORM","FORTY","FOX","FOXA","FRME","FRMI","FROG","FRSH","FSLR","FSV","FTAI","FTAIM","FTAIN","FTDR","FTNT","FULT","FULTP","FWONA","FWONK","FYBR","GBDC","GEHC","GEN","GFS","GH","GILD","GLBE","GLNG","GLPG","GLPI","GLXY","GMAB","GNTX","GOOG","GOOGL","GRAB","GRAL","GRFS","GSAT","GSHD","GT","GTLB","GTM","GTX","HALO","HAS","HBAN","HBANL","HBANM","HBANP","HCM","HLNE","HOLX","HON","HOOD","HQY","HSAI","HSIC","HST","HTFL","HTHT","HUBG","HURN","HUT","HWC","HWCPZ","HWKN","IAC","IBKR","IBOC","IBRX","ICLR","ICUI","IDCC","IDXX","IDYA","IEP","ILMN","IMVT","INCY","INDB","INDV","INSM","INTA","INTC","INTR","INTU","IONS","IPAR","IPGP","IQ","IREN","IRTC","ISRG","ITRI","JAZZ","JBHT","JD","JKHY","JOYY","KC","KDP","KHC","KLAC","KMB","KNSA","KRYS","KSPI","KTOS","KYIV","LAMR","LAUR","LBRDA","LBRDK","LBRDP","LBTYA","LBTYB","LBTYK","LCID","LECO","LEGN","LFST","LFUS","LGN","LI","LIF","LIN","LINE","LITE","LIVN","LKQ","LLYVA","LLYVK","LNT","LOGI","LOPE","LPLA","LRCX","LSCC","LSTR","LULU","LYFT","MANH","MAR","MASI","MAT","MBLY","MCHB","MCHP","MCHPP","MDGL","MDLZ","MEDP","MELI","MEOH","META","MFICL","MGEE","MGNI","MGRC","MIDD","MKSI","MKTX","MLCO","MLYS","MMSI","MMYT","MNDY","MNST","MORN","MPWR","MQ","MRCY","MRNA","MRVL","MRX","MSFT","MSTR","MTCH","MTSI","MU","MYRG","MZTI","NAVN","NBIS","NBIX","NBTB","NCNO","NDAQ","NDSN","NFLX","NICE","NMRK","NOVT","NSIT","NTAP","NTES","NTNX","NTRA","NTRS","NTRSO","NTSK","NUVL","NVDA","NVMI","NWE","NWS","NWSA","NXPI","NXST","NXT","ODFL","OKTA","OLED","OMAB","ON","ONB","ONBPO","ONBPP","ONC","OPCH","OPEN","ORLY","OS","OSIS","OTEX","OTTR","OXLC","OXLCL","OXLCN","OXLCO","OXLCP","OXLCZ","OZK","PAA","PAGP","PANW","PATK","PAX","PAYX","PCAR","PCH","PCTY","PCVX","PDD","PECO","PEGA","PEP","PFG","PGNY","PI","PINC","PLMR","PLTR","PLUS","PLXS","PNFP","PODD","PONY","POOL","POWL","PPC","PRAX","PRDO","PRVA","PSKY","PSMT","PTC","PTCT","PTEN","PTON","PTRN","PYPL","QCOM","QFIN","QLYS","QRVO","RARE","REG","REGCO","REGCP","REGN","RELY","REYN","RGEN","RGLD","RIVN","RMBS","RNW","ROAD","ROIV","ROKU","ROP","ROST","RPRX","RRR","RUN","RUSHA","RUSHB","RVMD","RXRX","RYAAY","SAIA","SAIC","SAIL","SANM","SATS","SBAC","SBCF","SBLK","SBRA","SBUX","SEDG","SEIC","SFD","SFM","SFNC","SHC","SHOO","SHOP","SIGI","SIMO","SIRI","SKYW","SLAB","SLDE","SLM","SLMBP","SMCI","SMTC","SNDK","SNEX","SNPS","SNY","SOFI","SOLS","SONO","SPNS","SPSC","SRAD","SRRK","SSNC","SSRM","STEP","STLD","STNE","STRC","STRD","STRF","STRK","STRL","STX","SWKS","SYNA","TARS","TBBK","TCBI","TCOM","TEAM","TECH","TEM","TENB","TER","TERN","TFSL","TIGO","TLN","TLX","TMC","TMUS","TOWN","TPG","TRI","TRMB","TRMD","TRMK","TROW","TSCO","TSEM","TSLA","TTAN","TTEK","TTMI","TTWO","TW","TXG","TXN","TXRH","UAL","UBSI","UFPI","ULTA","UMBF","UMBFO","UPST","UPWK","URBN","USLM","UTHR","VC","VCTR","VFS","VIAV","VICR","VLY","VLYPN","VLYPO","VLYPP","VNET","VNOM","VOD","VRNS","VRSK","VRSN","VRTX","VSAT","VSEC","VTRS","WAFD","WAY","WB","WBD","WDAY","WDC","WDFC","WFRD","WGS","WING","WIX","WMG","WSBC","WSBCO","WSBCP","WSFS","WTFC","WTW","WWD","WYNN","XEL","XMTR","XNET","XP","XRAY","Z","ZBRA","ZG","ZION","ZM","ZS","SPCE","APLD","CRWV","NBIS","AEHR","CMCO","SMCI","COIN","OKLO","ALB","NET","SOFI","GOOGL","FSLR","ONON","UNH","AI","INTC","EVTL","TEM","ISRG","DAVE","SNOW","EXEL","ARM","GFS","PATH","TTD","ALTS","SYNA","RBLX","SKYT","RIVN","NVTS","INOD","OSCR","IOT","DDOG","RKLB"]

print(f"Toplam {len(tickers)} hisse için piyasa verileri çekiliyor...")

market_data = {}

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        def get_info(key):
            val = info.get(key)
            return val if val is not None else 0

        price = get_info('currentPrice')
        
        # --- DÜZELTİLMİŞ MANTIK ---
        # 1. Önce Yahoo'nun hazır Forward P/E verisini çek (ALNY için doğrusu bu)
        forward_pe = info.get('forwardPE')
        
        # 2. Eğer Yahoo bu veriyi vermemişse (None ise), o zaman manuel hesapla (AMZN vb. için yedek)
        if forward_pe is None:
            eps = info.get('forwardEps')
            if eps and eps > 0:
                forward_pe = price / eps
            else:
                forward_pe = 0 # Hesaplayamıyorsak 0 dön
        # --------------------------

        # Hedef Fiyatı yuvarla (Örn: 293.03067 -> 293.03)
        target_price = get_info('targetMeanPrice')
        if target_price:
            target_price = round(target_price, 2)

        data = {
            "price": price,
            "mcap": get_info('marketCap'),
            "pe": get_info('trailingPE'),
            "forward_pe": forward_pe, # Artık hibrit mantık devrede
            "ev_ebitda": get_info('enterpriseToEbitda'),
            "pb": get_info('priceToBook'),
            "target": target_price,
            "recommendation": info.get('recommendationKey', 'none')
        }
        
        market_data[ticker] = data
        print(f"{ticker} OK: ${data['price']} | F_PE: {data['forward_pe']}")
        
        time.sleep(0.1)
        
    except Exception as e:
        print(f"Hata ({ticker}): {e}")

with open(os.path.join(DATA_FOLDER, "pazar_verileri.json"), 'w', encoding='utf-8') as f:
    json.dump(market_data, f, ensure_ascii=False)


print("\nBİTTİ! Veriler güncellendi.")
