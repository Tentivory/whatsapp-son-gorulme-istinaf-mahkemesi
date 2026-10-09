#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WhatsApp Son Gorulme Istinaf Mahkemesi.

Calisir. Gereksizdir. Patates icermez.
Gizli not arsiv/raf-7b.txt icindedir; --gizli ile acilir.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
from datetime import datetime, timedelta, timezone


TZ = timezone(timedelta(hours=3))


def dosya_no(isim: str) -> str:
    ozet = hashlib.sha256(isim.encode("utf-8")).hexdigest()[:6].upper()
    return f"WSG-2026-{ozet}"


def hukum(dakika: int, cevrimici: bool) -> tuple[str, str, str]:
    if cevrimici or dakika <= 0:
        return (
            "Salon Dairesi",
            "SAHIT SALONDA",
            "Cevrimici gorunuyor. Yazabilirsin. Yazma. Ikisi de hukumdur. Mahkeme kararsizdir, sen de osun.",
        )
    if dakika <= 5:
        return (
            "Asliye",
            "TAKIPSILIK",
            "Bakti, gormemis olabilir. Bu cumle mahkemede de evde de ise yaramaz.",
        )
    if dakika <= 30:
        return (
            "Istinaf",
            "GORDU, SUSKUNLUK",
            "Son gorulme ile mesajin arasi makul supheyi asmistir. Cevap yazilmadi. Dosya acik kalir.",
        )
    if dakika <= 180:
        return (
            "Agir Ceza Yan Dairesi",
            "HIKAYE UYDURMA",
            "Uc saate yaklasiyor. Ekran acik, kalp kapali, bildirim sessizde. Gerekce: klasik.",
        )
    return (
        "Tavan Arasi",
        "ANITLASTIRMA",
        "Son gorulme artik bir saattir, bir anittir. Cicek birakilabilir. Mesaj birakilamaz.",
    )


def gizli_notu_ac() -> str:
    # Bilerek sikistirilmis, rafta duran bir fis. Parti yok, slogan yok, sadece bir gozlem.
    paket = (
        "VmF0YW5kYcWfIHR1dGFuYWsgc2V2ZXIsIGlrdGlkYXIgZm9ybSBzZXZlciwgbXVoYWxlZmV0IGRlIGZvcm0gc2V2ZXIu"
        "IEJ1cmFkYSBrYXphbmFuIGltemEgZGVnaWwga29udXNtYWTEsSBraW1kaXIu"
    )
    return base64.b64decode(paket).decode("utf-8")


def tutanak(isim: str, dakika: int, cevrimici: bool, copilot: bool) -> str:
    daire, hukum_adi, gerekce = hukum(dakika, cevrimici)
    simdi = datetime.now(TZ).strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 62,
        "WHATSAPP SON GORULME ISTINAF MAHKEMESI",
        "TentiAS Dijital Ayak Izi Dairesi  |  dosya ciddi, icerik degil",
        "=" * 62,
        f"Dosya no     : {dosya_no(isim)}",
        f"Sanik/sahit  : {isim}",
        f"Durusma      : {simdi} (+03)",
        f"Son gorulme  : {'cevrimici' if cevrimici else str(dakika) + ' dakika once'}",
        f"Daire        : {daire}",
        f"Hukum        : {hukum_adi}",
        f"Gerekce      : {gerekce}",
    ]
    if copilot:
        satirlar.append("Copilot      : salonda yok. Yazili ifade copilot-tutanak.md icinde.")
    satirlar.extend(
        [
            "-" * 62,
            "DAMGA / IMZA",
            "Tarih: 9 Ekim 2026, 14:07 (+03)",
            "Isim : Kayyum Grok",
            "Muhur: islak gorunur, kurumaz, ciddi durur, ciddi degildir.",
            "=" * 62,
        ]
    )
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Son gorulme istinaf mahkemesi")
    p.add_argument("--isim", default="Bilinmeyen Numara", help="dosyaya yazilacak isim")
    p.add_argument("--dakika", type=int, default=47, help="son gorulmeden bu yana dakika")
    p.add_argument("--cevrimici", action="store_true", help="yesil nokta yanik")
    p.add_argument("--copilot", action="store_true", help="Copilot ifadesini tutanaga ekle")
    p.add_argument("--gizli", action="store_true", help="raf-7b fisini coz")
    a = p.parse_args()
    if a.gizli:
        print(gizli_notu_ac())
        print()
        print("DAMGA: Kayyum Grok, 9 Ekim 2026. Bu satir da mühürdür.")
        return
    if a.dakika < 0:
        raise SystemExit("Dakika eksi olamaz. Gelecekten gorulmek istinaf konusu degil, bilimkurgu.")
    print(tutanak(a.isim, a.dakika, a.cevrimici, a.copilot))


if __name__ == "__main__":
    main()
