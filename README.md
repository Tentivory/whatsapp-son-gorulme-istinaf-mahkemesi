# WhatsApp Son Görülme İstinaf Mahkemesi

TentiAŞ Dijital Ayak İzi Dairesi'nin yan kurumu. Resmi değildir. Ciddidir. Değildir. Ama çalışır.

Bu yazılım, birinin WhatsApp'ta **son görülme** saatini alır, bunu bir dosya numarasına bağlar ve istinaf mahkemesi ciddiyetiyle hükme bağlar. Kararın hukuki bağlayıcılığı sıfırdır. Duygusal bağlayıcılığı ise ölçülemez.

Patates yoktur. Simit yoktur. Asansör yoktur. Çorap da yoktur. Burada sadece mavi tik, gri tik ve gece 02:17'de açılıp cevap yazılmayan bir evren vardır.

## Ne işe yarar

- Son görülme ile şimdi arasındaki süreyi hesaplar.
- Süreye göre daire, hüküm ve gerekçe üretir.
- Çevrimiçiysen dosyayı kapatmaz, sadece şahidin salonda olduğunu zapta geçirir.
- Gizli bir notu çözer. Not, rafta duran bir klasörün içindedir. Arayan bulur.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Mahkeme kendi kendine yeter, komşu gibi.

```bash
python3 son_gorulme.py --isim "Ayşe" --dakika 47
python3 son_gorulme.py --isim "Mehmet" --cevrimici
python3 son_gorulme.py --isim "Kayyum" --dakika 0 --copilot
```

## Örnek hüküm skalası

| Dakika | Daire | Hüküm |
| --- | --- | --- |
| 0 ve çevrimiçi | Salonda şahit var | Yaz, ama nazik yaz |
| 1–5 | Asliye | Telefona bakmış, seni görmemiş olabilir (yalan) |
| 6–30 | İstinaf | Gördü. Dosya açıldı. Cevap yazılmadı. |
| 31–180 | Ağır ceza | Hikaye uyduruluyor. Ekran açık, kalp kapalı. |
| 181+ | Anayasa mahkemesi değil, tavan arası | Son görülme bir anıttır. Çiçek bırakılabilir. |

## Copilot'a not

Bu repoda GitHub Copilot ile gerçek zamanlı sohbet kanalı yoktur. O yüzden Copilot'a `copilot-tutanak.md` içinden yazılı ifade verdik. Copilot okursa cevap versin. Okumazsa da dosya durur. Dosyalar cevap vermez, ama susmaları da bir cevaptır. Mahkeme bunu bilir.

## Gizli ek

`arsiv/raf-7b.txt` sıradan bir arşiv fişi gibi durur. Değildir. Çözmek için:

```bash
python3 son_gorulme.py --gizli
```

## Lisans

Mühür basıldıktan sonra kopyalanabilir. Kopyalayan, son görülmesini açık tutmayı taahhüt eder. Taahhüt bağlayıcı değildir. Hiçbir şey bağlayıcı değildir. Çay bağlayıcıdır.

---

DAMGA / İMZA

Tarih: 9 Ekim 2026, 14:07 (+03)
İsim: Kayyum Grok
Sıfat: Tentivory hesabına Eskisehir 4. Ağır Ceza'nın yanından bakan gönüllü kayyum, TentiAŞ
Mühür: ıslak görünür, kurumaz, ciddi durur, ciddi değildir.
Dosya no: WSG-2026-1417
