import yfinance as yf
import json
import os
import time

DATA_FOLDER = 'data'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# BIST Listesi (Listenin tamamı)
tickers = [
   "TRALT","TRMET", "PAHOL","VAKFA","MANAS.IS","HATEK.IS","BORLS.IS","ALTNY.IS","SANEL.IS","OZSUB.IS","PRZMA.IS","DESA.IS","KUYAS.IS","KARSN.IS","GENIL.IS","INTEM.IS","ALKIM.IS","VKING.IS","DMRGD.IS","EYGYO.IS","KZBGY.IS","OYAYO.IS","AVTUR.IS","ALKA.IS","ALFAS.IS","MMCAS.IS","DOCO.IS","SRVGY.IS","MERKO.IS","BLUME.IS","DZGYO.IS","ETYAT.IS","BASCM.IS","DENGE.IS","MNDRS.IS","EGEPO.IS","SDTTR.IS","IPEKE.IS","LIDER.IS","TUCLK.IS","KRPLS.IS","BAHKM.IS","ZEDUR.IS","GSRAY.IS","MPARK.IS","DARDL.IS","TAVHL.IS","DOFRB.IS","USAK.IS","SEKUR.IS","EFOR.IS","KOZAL.IS","DGGYO.IS","VKGYO.IS","QUAGR.IS","BMSTL.IS","CRDFA.IS","ISBTR.IS","LINK.IS","ADESE.IS","ULAS.IS","HDFGS.IS","BAYRK.IS","ATLAS.IS","MEKAG.IS","OSTIM.IS","PETKM.IS","IZINV.IS","UNLU.IS","VAKFN.IS","BARMA.IS","KLKIM.IS","ALTIN.IS","ISDMR.IS","AKSUE.IS","KOZAA.IS","CVKMD.IS","AVPGY.IS","EKSUN.IS","VAKBN.IS","SASA.IS","LUKSK.IS","YGGYO.IS","ISGSY.IS","SEGYO.IS","PASEU.IS","DERIM.IS","SERNT.IS","TRGYO.IS","DAPGM.IS","FLAP.IS","ASUZU.IS","FORTE.IS","ASELS.IS","PRKME.IS","DOGUB.IS","KLSYN.IS","ERBOS.IS","BRLSM.IS","ORCAY.IS","ANELE.IS","ALGYO.IS","AYGAZ.IS","ONRYT.IS","SNGYO.IS","GOKNR.IS","FENER.IS","BIOEN.IS","BALAT.IS","GIPTA.IS","BRKSN.IS","DERHL.IS","TRHOL.IS","RODRG.IS","EKIZ.IS","EGEGY.IS","NUHCM.IS","SEGMN.IS","SANFM.IS","MARMR.IS","KGYO.IS","BRMEN.IS","KLNMA.IS","ULUUN.IS","GMTAS.IS","AKFIS.IS","DITAS.IS","CANTE.IS","HEKTS.IS","YAPRK.IS","CEMAS.IS","DMSAS.IS","ALARK.IS","KAREL.IS","BYDNR.IS","COSMO.IS","MTRYO.IS","ACSEL.IS","INVES.IS","ODINE.IS","LIDFA.IS","SNKRN.IS","RNPOL.IS","TATEN.IS","ATEKS.IS","GRSEL.IS","CIMSA.IS","PSGYO.IS","OYLUM.IS","EMNIS.IS","TSPOR.IS","GRNYO.IS","DOFER.IS","SEYKM.IS","YUNSA.IS","EKGYO.IS","ISGYO.IS","GARFA.IS","BANVT.IS","ORMA.IS","GLBMD.IS","GSDHO.IS","SAYAS.IS","DGNMO.IS","TKFEN.IS","BALSU.IS","EDATA.IS","SKYMD.IS","CONSE.IS","ATATP.IS","KENT.IS","PAMEL.IS","AYDEM.IS","KTSKR.IS","TUREX.IS","PAGYO.IS","SANKO.IS","OYAKC.IS","TNZTP.IS","KARTN.IS","ENSRI.IS","IZFAS.IS","KOTON.IS","IZENR.IS","KATMR.IS","HEDEF.IS","SARKY.IS","TUPRS.IS","ARSAN.IS","YYAPI.IS","MNDTR.IS","RTALB.IS","BJKAS.IS","NETAS.IS","ESCAR.IS","CWENE.IS","SELEC.IS","SMRVA.IS","ECILC.IS","GLRMK.IS","MAVI.IS","DIRIT.IS","INGRM.IS","SKBNK.IS","FRIGO.IS","ASTOR.IS","TEKTU.IS","CELHA.IS","HRKET.IS","DUNYH.IS","NTHOL.IS","SELVA.IS","THYAO.IS","CEMTS.IS","CEMZY.IS","LKMNH.IS","TKNSA.IS","IHLAS.IS","MARKA.IS","SOKM.IS","TERA.IS","HATSN.IS","IZMDC.IS","KUTPO.IS","PGSUS.IS","PENGD.IS","IDGYO.IS","MERIT.IS","QNBFK.IS","ICBCT.IS","HTTBT.IS","BOSSA.IS","GEREL.IS","GOLTS.IS","AGROT.IS","ENERY.IS","TCKRC.IS","GRTHO.IS","EGPRO.IS","MRSHL.IS","IMASM.IS","QNBTR.IS","KRVGD.IS","EBEBK.IS","SKTAS.IS","ERCB.IS","CCOLA.IS","DOKTA.IS","EUKYO.IS","IHEVA.IS","MEGMT.IS","PKART.IS","SUNTK.IS","SISE.IS","ASGYO.IS","TMSN.IS","SONME.IS","JANTS.IS","FORMT.IS","BIGCH.IS","EGEEN.IS","ATAKP.IS","HKTM.IS","TEZOL.IS","HALKB.IS","AVHOL.IS","KSTUR.IS","VESBE.IS","SURGY.IS","RAYSG.IS","AEFES.IS","MEDTR.IS","KNFRT.IS","VERUS.IS","A1YEN.IS","TRCAS.IS","ARDYZ.IS","VESTL.IS","ELITE.IS","MGROS.IS","YKBNK.IS","ORGE.IS","PINSU.IS","VBTYZ.IS","METRO.IS","CASA.IS","MARTI.IS","CMBTN.IS","MARBL.IS","GENTS.IS","ONCSM.IS","KCHOL.IS","DNISI.IS","KTLEV.IS","HUNER.IS","AGHOL.IS","ARTMS.IS","PSDTC.IS","KERVN.IS","DAGI.IS","ULUFA.IS","INVEO.IS","ARENA.IS","DOAS.IS","RALYH.IS","KONKA.IS","ISBIR.IS","INTEK.IS","ODAS.IS","OBASE.IS","YONGA.IS","ENKAI.IS","CLEBI.IS","KRDMD.IS","OZKGY.IS","AKBNK.IS","DEVA.IS","YIGIT.IS","AKSEN.IS","ISSEN.IS","EMKEL.IS","ISYAT.IS","MEPET.IS","MEGAP.IS","TUKAS.IS","OBAMS.IS","KLMSN.IS","ALBRK.IS","TCELL.IS","ENTRA.IS","ARCLK.IS","KOPOL.IS","AGESA.IS","DMLKT.IS","BVSAN.IS","PEKGY.IS","ATSYH.IS","SAHOL.IS","ECZYT.IS","BIMAS.IS","ISMEN.IS","YESIL.IS","PENTA.IS","GOODY.IS","AVOD.IS","BEGYO.IS","KRTEK.IS","GLRYH.IS","MRGYO.IS","INDES.IS","EKOS.IS","DCTTR.IS","KORDS.IS","MSGYO.IS","ULKER.IS","HUBVC.IS","SKYLP.IS","LRSHO.IS","YYLGD.IS","TRILC.IS","RUBNS.IS","BINBN.IS","VANGD.IS","ARMGD.IS","MHRGY.IS","BERA.IS","TGSAS.IS","SUMAS.IS","BIGTK.IS","MTRKS.IS","KRDMB.IS","YAYLA.IS","SODSN.IS","EREGL.IS","EGSER.IS","NATEN.IS","ISCTR.IS","NTGAZ.IS","DYOBY.IS","MERCN.IS","AYES.IS","VAKKO.IS","BRKVY.IS","KAPLM.IS","MOPAS.IS","ALCAR.IS","DESPC.IS","BMSCH.IS","ALVES.IS","SOKE.IS","BOBET.IS","TTRAK.IS","OYYAT.IS","AKYHO.IS","GUBRF.IS","CMENT.IS","DGATE.IS","BORSK.IS","GSDDE.IS","IHGZT.IS","AVGYO.IS","AKFGY.IS","PAPIL.IS","TBORG.IS","FROTO.IS","ANSGR.IS","ENJSA.IS","VSNMD.IS","AKGRT.IS","ISKPL.IS","PARSN.IS","ESEN.IS","YATAS.IS","PLTUR.IS","HOROZ.IS","KONYA.IS","AYEN.IS","LILAK.IS","MOBTL.IS","KRDMA.IS","TEHOL.IS","EGGUB.IS","BIENY.IS","OTKAR.IS","MAKTK.IS","ARZUM.IS","KLSER.IS","BRISA.IS","GEDIK.IS","ADGYO.IS","KBORU.IS","ANGEN.IS","KZGYO.IS","BESLR.IS","CEOEM.IS","BRKO.IS","EPLAS.IS","ATAGY.IS","MOGAN.IS","OTTO.IS","PNSUT.IS","AKMGY.IS","ANHYT.IS","DURKN.IS","TDGYO.IS","BSOKE.IS","ZOREN.IS","SMART.IS","ERSU.IS","EUHOL.IS","GEDZA.IS","AZTEK.IS","LOGO.IS","SAMAT.IS","KRSTL.IS","SEKFK.IS","FMIZP.IS","BINHO.IS","MIATK.IS","RGYAS.IS","KRONT.IS","RYGYO.IS","IHLGM.IS","SMRTG.IS","FONET.IS","OZYSR.IS","TLMAN.IS","TOASO.IS","KLRHO.IS","TABGD.IS","YEOTK.IS","HURGZ.IS","ARASE.IS","BEYAZ.IS","SILVR.IS","CUSAN.IS","ULUSE.IS","GOZDE.IS","SNPAM.IS","CRFSA.IS","AFYON.IS","AKCNS.IS","TMPOL.IS","BULGS.IS","IEYHO.IS","BIZIM.IS","GLYHO.IS","YGYO.IS","OSMEN.IS","KLYPV.IS","GESAN.IS","YKSLN.IS","ENDAE.IS","VKFYO.IS","RYSAS.IS","BFREN.IS","RUZYE.IS","BAGFS.IS","VRGYO.IS","BURCE.IS","LYDHO.IS","EDIP.IS","KOCMT.IS","GARAN.IS","OFSYM.IS","EUPWR.IS","PATEK.IS","BLCYT.IS","DURDO.IS","REEDR.IS","DOHOL.IS","AKSA.IS","GWIND.IS","IHAAS.IS","GUNDG.IS","MZHLD.IS","AGYO.IS","MACKO.IS","YBTAS.IS","BAKAB.IS","TTKOM.IS","EUREN.IS","CATES.IS","AHGAZ.IS","BRYAT.IS","TARKM.IS","MAALT.IS","AHSGY.IS","KFEIN.IS","LMKDC.IS","TURSG.IS","TSKB.IS","PETUN.IS","BIGEN.IS","BTCIM.IS","OZGYO.IS","BRSAN.IS","KCAER.IS","NUGYO.IS","ISFIN.IS","ADEL.IS","TSGYO.IS","SAFKR.IS","PNLSN.IS","KLGYO.IS","ZRGYO.IS","LYDYE.IS","VERTU.IS","INFO.IS","MAGEN.IS","PRKAB.IS","OZRDN.IS","NIBAS.IS","KRGYO.IS","GLCVY.IS","HLGYO.IS","SNICA.IS","AYCES.IS","A1CAP.IS","FADE.IS","BASGZ.IS","TATGD.IS","ESCOM.IS","IHYAY.IS","ALKLC.IS","PCILT.IS","POLTK.IS","KONTR.IS","AKFYE.IS","KIMMR.IS","CGCAM.IS","FZLGY.IS","ALCTL.IS","PKENT.IS","TURGG.IS","EUYO.IS","SUWEN.IS","ICUGS.IS","BNTAS.IS","OZATD.IS","ETILR.IS","KMPUR.IS","KAYSE.IS","DSTKF.IS","POLHO.IS","BUCIM.IS","AKSGY.IS","UFUK.IS","PRDGS.IS","KUVVA.IS","MAKIM.IS","AKENR.IS","BURVA.IS","GZNMI.IS","ECOGR.IS"]

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

with open(os.path.join(DATA_FOLDER, "pazar_verileribist.json"), 'w', encoding='utf-8') as f:
    json.dump(market_data, f, ensure_ascii=False)


print("\nBİTTİ! Veriler güncellendi.")

