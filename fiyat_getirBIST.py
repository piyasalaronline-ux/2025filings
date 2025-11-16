import yfinance as yf
import json
import os
import time

DATA_FOLDER = 'data'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# BIST Listesi (Listenin tamamı)
tickers = [
    "MANAS","HATEK","BORLS","ALTNY","SANEL","OZSUB","PRZMA","DESA","KUYAS","KARSN","GENIL","INTEM","ALKIM","VKING","DMRGD","EYGYO","KZBGY","OYAYO","AVTUR","ALKA","ALFAS","MMCAS","DOCO","SRVGY","MERKO","BLUME","DZGYO","ETYAT","BASCM","DENGE","MNDRS","EGEPO","SDTTR","IPEKE","LIDER","TUCLK","KRPLS","BAHKM","ZEDUR","GSRAY","MPARK","DARDL","TAVHL","DOFRB","USAK","SEKUR","EFOR","KOZAL","DGGYO","VKGYO","QUAGR","BMSTL","CRDFA","ISBTR","LINK","ADESE","ULAS","HDFGS","BAYRK","ATLAS","MEKAG","OSTIM","PETKM","IZINV","UNLU","VAKFN","BARMA","KLKIM","ALTIN","ISDMR","AKSUE","KOZAA","CVKMD","AVPGY","EKSUN","VAKBN","SASA","LUKSK","YGGYO","ISGSY","SEGYO","PASEU","DERIM","SERNT","TRGYO","DAPGM","FLAP","ASUZU","FORTE","ASELS","PRKME","DOGUB","KLSYN","ERBOS","BRLSM","ORCAY","ANELE","ALGYO","AYGAZ","ONRYT","SNGYO","GOKNR","FENER","BIOEN","BALAT","GIPTA","BRKSN","DERHL","TRHOL","RODRG","EKIZ","EGEGY","NUHCM","SEGMN","SANFM","MARMR","KGYO","BRMEN","KLNMA","ULUUN","GMTAS","AKFIS","DITAS","CANTE","HEKTS","YAPRK","CEMAS","DMSAS","ALARK","KAREL","BYDNR","COSMO","MTRYO","ACSEL","INVES","ODINE","LIDFA","SNKRN","RNPOL","TATEN","ATEKS","GRSEL","CIMSA","PSGYO","OYLUM","EMNIS","TSPOR","GRNYO","DOFER","SEYKM","YUNSA","EKGYO","ISGYO","GARFA","BANVT","ORMA","GLBMD","GSDHO","SAYAS","DGNMO","TKFEN","BALSU","EDATA","SKYMD","CONSE","ATATP","KENT","PAMEL","AYDEM","KTSKR","TUREX","PAGYO","SANKO","OYAKC","TNZTP","KARTN","ENSRI","IZFAS","KOTON","IZENR","KATMR","HEDEF","SARKY","TUPRS","ARSAN","YYAPI","MNDTR","RTALB","BJKAS","NETAS","ESCAR","CWENE","SELEC","SMRVA","ECILC","GLRMK","MAVI","DIRIT","INGRM","SKBNK","FRIGO","ASTOR","TEKTU","CELHA","HRKET","DUNYH","NTHOL","SELVA","THYAO","CEMTS","CEMZY","LKMNH","TKNSA","IHLAS","MARKA","SOKM","TERA","HATSN","IZMDC","KUTPO","PGSUS","PENGD","IDGYO","MERIT","QNBFK","ICBCT","HTTBT","BOSSA","GEREL","GOLTS","AGROT","ENERY","TCKRC","GRTHO","EGPRO","MRSHL","IMASM","QNBTR","KRVGD","EBEBK","SKTAS","ERCB","CCOLA","DOKTA","EUKYO","IHEVA","MEGMT","PKART","SUNTK","SISE","ASGYO","TMSN","SONME","JANTS","FORMT","BIGCH","EGEEN","ATAKP","HKTM","TEZOL","HALKB","AVHOL","KSTUR","VESBE","SURGY","RAYSG","AEFES","MEDTR","KNFRT","VERUS","A1YEN","TRCAS","ARDYZ","VESTL","ELITE","MGROS","YKBNK","ORGE","PINSU","VBTYZ","METRO","CASA","MARTI","CMBTN","MARBL","GENTS","ONCSM","KCHOL","DNISI","KTLEV","HUNER","AGHOL","ARTMS","PSDTC","KERVN","DAGI","ULUFA","INVEO","ARENA","DOAS","RALYH","KONKA","ISBIR","INTEK","ODAS","OBASE","YONGA","ENKAI","CLEBI","KRDMD","OZKGY","AKBNK","DEVA","YIGIT","AKSEN","ISSEN","EMKEL","ISYAT","MEPET","MEGAP","TUKAS","OBAMS","KLMSN","ALBRK","TCELL","ENTRA","ARCLK","KOPOL","AGESA","DMLKT","BVSAN","PEKGY","ATSYH","SAHOL","ECZYT","BIMAS","ISMEN","YESIL","PENTA","GOODY","AVOD","BEGYO","KRTEK","GLRYH","MRGYO","INDES","EKOS","DCTTR","KORDS","MSGYO","ULKER","HUBVC","SKYLP","LRSHO","YYLGD","TRILC","RUBNS","BINBN","VANGD","ARMGD","MHRGY","BERA","TGSAS","SUMAS","BIGTK","MTRKS","KRDMB","YAYLA","SODSN","EREGL","EGSER","NATEN","ISCTR","NTGAZ","DYOBY","MERCN","AYES","VAKKO","BRKVY","KAPLM","MOPAS","ALCAR","DESPC","BMSCH","ALVES","SOKE","BOBET","TTRAK","OYYAT","AKYHO","GUBRF","CMENT","DGATE","BORSK","GSDDE","IHGZT","AVGYO","AKFGY","PAPIL","TBORG","FROTO","ANSGR","ENJSA","VSNMD","AKGRT","ISKPL","PARSN","ESEN","YATAS","PLTUR","HOROZ","KONYA","AYEN","LILAK","MOBTL","KRDMA","TEHOL","EGGUB","BIENY","OTKAR","MAKTK","ARZUM","KLSER","BRISA","GEDIK","ADGYO","KBORU","ANGEN","KZGYO","BESLR","CEOEM","BRKO","EPLAS","ATAGY","MOGAN","OTTO","PNSUT","AKMGY","ANHYT","DURKN","TDGYO","BSOKE","ZOREN","SMART","ERSU","EUHOL","GEDZA","AZTEK","LOGO","SAMAT","KRSTL","SEKFK","FMIZP","BINHO","MIATK","RGYAS","KRONT","RYGYO","IHLGM","SMRTG","FONET","OZYSR","TLMAN","TOASO","KLRHO","TABGD","YEOTK","HURGZ","ARASE","BEYAZ","SILVR","CUSAN","ULUSE","GOZDE","SNPAM","CRFSA","AFYON","AKCNS","TMPOL","BULGS","IEYHO","BIZIM","GLYHO","YGYO","OSMEN","KLYPV","GESAN","YKSLN","ENDAE","VKFYO","RYSAS","BFREN","RUZYE","BAGFS","VRGYO","BURCE","LYDHO","EDIP","KOCMT","GARAN","OFSYM","EUPWR","PATEK","BLCYT","DURDO","REEDR","DOHOL","AKSA","GWIND","IHAAS","GUNDG","MZHLD","AGYO","MACKO","YBTAS","BAKAB","TTKOM","EUREN","CATES","AHGAZ","BRYAT","TARKM","MAALT","AHSGY","KFEIN","LMKDC","TURSG","TSKB","PETUN","BIGEN","BTCIM","OZGYO","BRSAN","KCAER","NUGYO","ISFIN","ADEL","TSGYO","SAFKR","PNLSN","KLGYO","ZRGYO","LYDYE","VERTU","INFO","MAGEN","PRKAB","OZRDN","NIBAS","KRGYO","GLCVY","HLGYO","SNICA","AYCES","A1CAP","FADE","BASGZ","TATGD","ESCOM","IHYAY","ALKLC","PCILT","POLTK","KONTR","AKFYE","KIMMR","CGCAM","FZLGY","ALCTL","PKENT","TURGG","EUYO","SUWEN","ICUGS","BNTAS","OZATD","ETILR","KMPUR","KAYSE","DSTKF","POLHO","BUCIM","AKSGY","UFUK","PRDGS","KUVVA","MAKIM","AKENR","BURVA","GZNMI","ECOGR"
]

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