#Program:
urun_adi=input("ürün adını giriniz:")
onceki_fiyat=float(input("ürünün geçen ayki fiyatını giriniz:")) #fiyat (para birimi) verileri, reel sayı (float) olmalıdır!
simdiki_fiyat=float(input("ürünün bu ayki fiyatını giriniz:"))

fiyat_farki=simdiki_fiyat-onceki_fiyat
fiyat_degisim_orani=fiyat_farki*100/onceki_fiyat

print(f"{urun_adi} ürününün fiyatındaki aylık değişim;")
print(f"miktarı: {fiyat_farki:.2f} TL")
print(f"oranı: % {fiyat_degisim_orani:.2f}")
