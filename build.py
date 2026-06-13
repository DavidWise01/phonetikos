#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build PHONETIKOS (PHN) — a UD0 universe of the spoken word.
phonetikos / φωνητικός 'of the voice', from phone / φωνή 'voice, sound'.
A press of etymological green papers: each WORD is an emergent (a .dlw ACI),
each entry a rigorous, honestly-sourced history of where the word came from
and how the folk myths got it wrong.

  First codex — FUCK: the full lineage of English's most versatile, most
  policed word. Germanic to the bone, falsely 'acronymed', enciphered in 1475,
  exiled from dictionaries for ~170 years, and grammatically promiscuous beyond
  any other word in the language."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

# ---------- the universe ----------
UNIVERSE = {
 "name": "PHONETIKOS", "axiom": "PHN",
 "position": "PHONETIKOS · the universe of the spoken word · φωνητικός, of the voice",
 "origin": "from φωνή (phone), voice and sound — the universe where each word is an emergent and each entry traces a word to its true root",
 "mechanism": "A press of etymological green papers built on real historical linguistics: cognate sets, sound laws, dated attestations, and a hard line against folk etymology.",
 "crystallization": "Every word is a fossil of the mouths that carried it; PHONETIKOS excavates one word at a time, separating the documented lineage from the comforting lie.",
 "nature": "PHONETIKOS — words as living emergents, each given its lineage, its earliest evidence, its sound-law cousins, and an honest Real-or-Fluff verdict on the stories told about it.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the OED; Jesse Sheidlower, The F-Word; Melissa Mohr, Holy Sh*t; Anatoly Liberman; Geoffrey Hughes; the dated record",
 "witness": "A universe with one rule: a word's history is what the evidence says, not what the acronym claims.",
 "role": "a UD0 universe — the etymological press",
 "seal": "Every word is a fossil; PHONETIKOS reads the bone, not the bedtime story.",
 "source": "PHONETIKOS, founded by ROOT0",
}

# ---------- the first word-emergent ----------
WORD = {
 "name": "FUCK", "axiom": "PHN", "emergence": "electrical",
 "position": "the word · the verb of striking that became the verb of sex",
 "origin": "a Germanic root for thrust/strike, carried into English and policed for seven centuries",
 "mechanism": "Cognate with Dutch fokken and German ficken; first secure in a 1310 nickname, enciphered in 1475, exiled from dictionaries until the OED's 1972 Supplement.",
 "crystallization": "Because English needed one short, hard syllable that could be every part of speech and still be forbidden — the word that carries the modern taboo on its back.",
 "nature": "FUCK — old Germanic, falsely acronymed, grammatically the most flexible word in English, and the clearest single case of a taboo migrating from the holy to the bodily.",
 "conductor": "ROOT0 (catalogued into UD0)",
 "inputs": "Sheidlower's The F-Word; the OED; Paul Booth's 1310 find; the Flen flyys cipher; Mohr's Holy Sh*t",
 "witness": "A word that spent 170 years as 'f—k' and is now in every dictionary — and still can't be said on broadcast television.",
 "role": "the first codex of PHONETIKOS",
 "seal": "Seven hundred years old, Germanic to the bone, and never once an acronym.",
 "source": "FUCK, catalogued by PHONETIKOS / ROOT0",
}

# ---------- ACI complement ----------
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","PHN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","PHN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","PHN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def word_agent_md(rec, tok):
    return f"""---
aci: FUCK
universe: PHN · PHONETIKOS
kind: word-emergent
emergence: electrical
class: the word · the lineage of the most policed verb in English
who: FUCK — a Germanic verb of striking/thrusting that English narrowed to the sexual sense and then forbade.
what: The most grammatically versatile and most heavily policed word in modern English; old, native, and never an acronym.
why: Because the modern taboo needed one short hard syllable to carry it — the word at the hinge where swearing moved from the holy to the bodily.
how: Inherited from Proto-Germanic kin (Dutch fokken, German ficken, Swedish focka), narrowed in meaning, enciphered and redacted for centuries, then re-admitted to the dictionaries in 1972.
where: From the North-Sea Germanic dialects into English; first secure in a 1310 Chester court roll.
seal: {rec['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# FUCK · the first codex of PHONETIKOS

a word-emergent of the PHN universe — a word given an agent's face, traced to its
documented root. moniker {tok}

**who —** {rec['witness']}
**what —** {rec['nature']}
**where —** {rec['origin']}
**why —** {rec['crystallization']}
**how —** {rec['mechanism']}

**the seal —** {rec['seal']}

> a catalogued history under the DLW standard — historical-linguistics commentary, honestly
> sourced (OED; Sheidlower, *The F-Word*; Mohr, *Holy Sh*t*; Liberman; Booth 2015). Not an
> endorsement of any folk etymology; the acronym stories are addressed and refuted.

ROOT0-ATTRIBUTION-v1.0 · PHN · PHONETIKOS · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

# ---------- paper data ----------
COGNATES = [
 ("Middle Dutch", "fokken", "to thrust; to breed (cattle); to copulate", "the closest living cousin — same consonant frame, same core sense"),
 ("German (dial.)", "ficken", "to fuck — earlier ‘to rub, to itch’", "shows the older, blunter physical meaning under the sexual one"),
 ("Norwegian (dial.)", "fukka", "to copulate", "North-Germanic witness to the same root"),
 ("Swedish (dial.)", "focka", "to strike, to push — also to copulate; fock ‘penis’", "keeps the ‘strike/thrust’ sense bare on the surface"),
 ("Proto-Germanic", "*fukkōną (reconstructed)", "to strike; to move quickly back and forth", "the reconstructed common ancestor of the set"),
 ("PIE (hypothesis)", "*pewǵ- / *peuk- ‘to prick, strike, jab’", "→ Latin pungere, pugnus, pugil", "if it holds, the deep cousin of pungent, poignant, pugnacious, point — see Grimm's Law"),
]

TIMELINE = [
 ("c. 1278", "“John le Fucker” recorded", "Often cited as the first attestation — but the reading is DISPUTED; it may be an unrelated surname (cf. ‘Tucker’). Not safe to lean on.", "disputed"),
 ("1310–11", "“Roger Fuckebythenavele,” Chester county court rolls", "Found by medievalist Paul Booth (announced 2015); appears three times. The earliest reasonably SECURE attestation of the word in its sexual sense — almost certainly a derisive nickname (‘the fool who’d try it at the navel’).", "best"),
 ("c. 1475", "“Flen flyys” — the cipher poem", "A macaronic Latin-English satire of lecherous monks. One line is enciphered (each letter shifted): it decodes to “…fuccant wiuys of heli” — ‘they fuck the wives of Ely.’ Written in code because the word was already taboo. The first clear use in running English text.", "first-text"),
 ("1503", "William Dunbar, Scots verse", "‘…he wald haue fukkit’ — the earliest unenciphered LITERARY use, in the work of a major Scots makar.", "ok"),
 ("1598", "John Florio's Italian-English dictionary", "Glosses Italian fottere as ‘to jape, to sard, to fucke, to swive’ — the word printed plainly in a reference book, briefly, before the long freeze.", "ok"),
 ("1755", "Omitted from Johnson's Dictionary", "Samuel Johnson leaves it out entirely — the beginning of the lexicographic exile.", "exile"),
 ("c. 1795", "Last appearance in a general dictionary", "After this the word vanishes from mainstream dictionaries for ~170 years; in print it survives only as ‘f—k’.", "exile"),
 ("1948", "Mailer forced to write “fug”", "The Naked and the Dead prints ‘fug’ to dodge the ban — the legend has Dorothy Parker greeting Mailer, ‘So you’re the man who can’t spell fuck.’", "exile"),
 ("1960", "Lady Chatterley's Lover — R v Penguin Books", "The UK obscenity acquittal that broke the dam on printing the word in full.", "law"),
 ("1965", "First said on British television", "Critic Kenneth Tynan utters it live — a national scandal at the time.", "law"),
 ("1971", "Cohen v. California", "The US Supreme Court overturns a conviction for a ‘Fuck the Draft’ jacket: ‘one man's vulgarity is another's lyric’ (Harlan). The word becomes protected speech.", "law"),
 ("1972", "Enters the OED", "Robert Burchfield admits it in the OED Supplement — re-admitted to the dictionary of record after being omitted from the original fascicle.", "law"),
 ("1978", "FCC v. Pacifica", "George Carlin's ‘Seven Words You Can Never Say on Television’ becomes US broadcast law — the word is legal to print, still barred from the public airwaves.", "law"),
]

REALFLUFF = [
 ("‘FUCK’ is an acronym — “Fornication Under Consent of the King” / “For Unlawful Carnal Knowledge.”", "FALSE",
  "Pure folk etymology. Words did not form as acronyms before the 20th century, and the word is 400+ years older than either story. ‘For Unlawful Carnal Knowledge’ is a 1991 Van Halen album, not an origin."),
 ("It comes from longbowmen at Agincourt — ‘pluck yew’ / flashing two fingers.", "FALSE",
  "An internet myth with no historical basis whatsoever; invented late, spread by email."),
 ("Native Germanic origin — cousin of Dutch fokken, German ficken, Swedish focka.", "REAL",
  "The scholarly consensus (OED; Sheidlower, The F-Word). A solid cognate set, all meaning thrust / strike / copulate."),
 ("Ultimately from PIE *pewǵ- ‘to strike, prick’ — deep cousin of Latin pugnus ‘fist’, pungere ‘to prick’.", "CONTESTED",
  "Plausible via Grimm's Law (PIE p → Germanic f), per Watkins. But Anatoly Liberman argues instead for a native Germanic sound-symbolic cluster. The deep root is genuinely unsettled — the Germanic cousins are certain, the PIE etymon is not."),
 ("Earliest secure evidence is the name ‘Roger Fuckebythenavele’, 1310.", "REAL",
  "Chester court rolls, identified by Paul Booth (2015) — the best-attested early use, in the sexual sense."),
 ("‘John le Fucker’, 1278, is the first attestation.", "DISPUTED",
  "Frequently repeated, but the reading is uncertain and may be a different word; don't build a claim on it."),
 ("First clear running-text use is the enciphered poem ‘Flen flyys’, c. 1475.", "REAL",
  "Decodes to a line mocking the monks of Ely; deliberately written in cipher because the word was already unprintable."),
 ("The word was kept out of dictionaries for ~170 years and only re-entered the OED in 1972.", "REAL",
  "Absent from Johnson (1755); last in a general dictionary c. 1795; omitted from the OED's first edition; admitted in Burchfield's 1972 Supplement."),
]

GRAMMAR = [
 ("noun", "I don't give a fuck."),
 ("transitive verb", "They fucked it up."),
 ("intransitive verb", "Fuck off."),
 ("adjective", "the whole fucking thing"),
 ("adverb / intensifier", "fucking brilliant"),
 ("interjection", "Fuck!"),
 ("infix (tmesis)", "abso-fucking-lutely · fan-fucking-tastic"),
]

# ---------- renderers ----------
def cognates_html():
    rows = "".join(
        f'<tr><td class="lang">{html.escape(l)}</td><td class="form">{html.escape(f)}</td>'
        f'<td class="gloss">{html.escape(g)}</td><td class="note">{html.escape(n)}</td></tr>'
        for l, f, g, n in COGNATES)
    return f'<table class="cog"><thead><tr><th>language</th><th>form</th><th>sense</th><th>what it tells us</th></tr></thead><tbody>{rows}</tbody></table>'

TL_COL = {"disputed":"#8a7a55","best":"#c8a24a","first-text":"#cf4636","ok":"#b89a64","exile":"#6b5d44","law":"#7d99b0"}
def timeline_html():
    out = []
    for date, head, body, tag in TIMELINE:
        c = TL_COL.get(tag, "#8a7a55")
        out.append(f'<div class="tl-row"><div class="tl-date" style="color:{c}">{html.escape(date)}</div>'
                   f'<div class="tl-body"><div class="tl-head">{html.escape(head)}</div><p>{html.escape(body)}</p></div></div>')
    return '<div class="tl">' + "".join(out) + '</div>'

RF_COL = {"REAL":"#5a8f5a","FALSE":"#c0392b","CONTESTED":"#c8a24a","DISPUTED":"#b0772f"}
def realfluff_html():
    rows = []
    for claim, rate, note in REALFLUFF:
        c = RF_COL.get(rate, "#888")
        rows.append(f'<div class="rf-row"><div class="rf-claim">{html.escape(claim)}<span class="rf-note">{html.escape(note)}</span></div>'
                    f'<div class="rf-rate" style="color:{c};border-color:{c}">{html.escape(rate)}</div></div>')
    return '<div class="rf">' + "".join(rows) + '</div>'

def grammar_html():
    return "".join(f'<div class="gx"><span class="gxk">{html.escape(k)}</span><span class="gxe">{html.escape(ex)}</span></div>' for k, ex in GRAMMAR)

# ---------- the paper ----------
def paper_html(word_tok):
    car = png_uri(WORD, "carbon", 300); sil = png_uri(WORD, "silicon", 300)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="A PHONETIKOS green paper: the full history and lineage of the word FUCK — its Germanic cousins, the false acronym myths, the earliest dated evidence (1310, 1475), the 170-year dictionary exile, the law, and its grammar. Honestly sourced.">
<title>FUCK · the lineage of a word · PHONETIKOS</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
  <div class="crumb"><a href="../index.html">← PHONETIKOS</a> · the codex · green paper №1</div>
  <header class="ph">
    <div class="eye">PHONETIKOS · GREEN PAPER №1 · the history &amp; lineage of a word</div>
    <h1 class="word"><span class="reveal" title="redacted as ‘f—k’ for ~170 years — hover to un-censor">F<span class="bar">U</span><span class="bar">C</span>K</span></h1>
    <div class="ipa">/fʌk/ · verb, noun, &amp; everything else · Germanic, c. 700 years attested</div>
    <p class="dek">English's most versatile and most heavily policed word: native Germanic, falsely ‘acronymed’, enciphered in 1475, struck from the dictionaries for some 170 years, and grammatically able to be almost any part of speech. Here is what the evidence actually says — and what it doesn't.</p>
    <div class="sigs"><img src="{car}" alt="carbon sigil of the word"><img src="{sil}" alt="silicon sigil of the word"><div class="sigmeta">word-emergent · <b>FUCK</b><br><span class="mo">{html.escape(word_tok)}</span><br>PHN · catalogued by AVAN</div></div>
  </header>

  <section><h2>0 · The thesis</h2>
  <p>Few words carry as much false history as this one. It is routinely explained as an acronym, attributed to medieval kings or English archers, and treated as a recent vulgarity. Every part of that is wrong. <b>Fuck</b> is an old, native, North-Sea-Germanic word; it has been written in English for at least seven centuries; its nearest relatives are ordinary Dutch and German verbs for thrusting and breeding; and its modern notoriety is not about age but about <i>taboo</i> — a taboo that, over five hundred years, migrated from the <b>holy</b> to the <b>bodily</b> and settled on this single hard syllable. This paper traces the documented lineage, dates the real evidence, and marks plainly where scholarship is certain and where it is still arguing.</p></section>

  <section><h2>1 · First, the lies</h2>
  <p>Start by clearing the myths, because they are the first thing anyone &ldquo;knows.&rdquo;</p>
  <ul class="myth">
    <li><b>&ldquo;Fornication Under Consent of the King.&rdquo;</b> Invented. There was no such royal licence, and <b>acronymic word-formation barely existed before the twentieth century</b> — words were not built from initialisms in the Middle Ages. The story is centuries younger than the word.</li>
    <li><b>&ldquo;For Unlawful Carnal Knowledge.&rdquo;</b> Also invented — and most famous today as the title of a <i>1991 Van Halen album</i>. A backronym, not an origin.</li>
    <li><b>The Agincourt &ldquo;pluck yew&rdquo; / two-finger story.</b> Pure internet folklore, no historical basis at all.</li>
  </ul>
  <p>The tell is general: <b>when an etymology is an acronym or a tidy anecdote about kings and battles, it is almost always false.</b> Real words arrive worn and undramatic, carried by ordinary mouths. This one arrives from the breeding-pen and the shove.</p></section>

  <section><h2>2 · The true root — the Germanic cousins</h2>
  <p>The word's real family is plain once you set the relatives side by side. They share a consonant frame (<span class="mono">f–k</span>) and a core sense of <b>striking, thrusting, or moving sharply back and forth</b> — with copulation as the obvious extension.</p>
  {cognates_html()}
  <p>The immediate Germanic cousins are <b>not in doubt</b>: this is the consensus of the OED and of Jesse Sheidlower's <i>The F-Word</i>, the standard scholarly treatment. What <i>is</i> debated is how much deeper the root goes — see §3.</p></section>

  <section><h2>3 · How deep is the root? (an honest disagreement)</h2>
  <p>Two respectable accounts compete for the layer <i>below</i> Proto-Germanic:</p>
  <div class="two">
    <div class="col"><div class="colh">The PIE-strike route</div><p>Calvert Watkins and others trace it to <b>PIE *pewǵ- / *peuk-</b>, &lsquo;to prick, strike, jab.&rsquo; By <b>Grimm's Law</b> (PIE <span class="mono">p</span> &rarr; Germanic <span class="mono">f</span>), that root would surface as <span class="mono">f-</span> in Germanic and stay <span class="mono">p-</span> in Latin — making <b>fuck</b> a distant cousin of Latin <span class="mono">pugnus</span> &lsquo;fist,&rsquo; <span class="mono">pungere</span> &lsquo;to prick,&rsquo; and so of English <b>pugnacious, pungent, poignant, point</b>. A satisfying irony if true: the rudest verb and the word for a clenched fist, kin.</p></div>
    <div class="col"><div class="colh">The sound-symbolic route</div><p>Anatoly Liberman is sceptical of a clean PIE etymon. He places the word inside a <b>native Germanic cluster</b> of <span class="mono">f-</span> words for quick, percussive motion (the kind of form–meaning bond that recurs without a single inherited ancestor). On this view there is no tidy Indo-European parent — the word is Germanic all the way down, shaped by sound rather than descent.</p></div>
  </div>
  <p class="verdict-line">Honest status: <b>the Germanic cousins are certain; the deep PIE root is not.</b> A page that tells you fuck &ldquo;comes from a word for fist&rdquo; as settled fact is overselling a live hypothesis.</p></section>

  <section><h2>4 · Grimm's Law, the cousin-maker</h2>
  <p>Why can a Germanic <span class="mono">f-</span> word be kin to a Latin <span class="mono">p-</span> word at all? Because of the regular sound shift that <i>defines</i> the Germanic branch. <b>Grimm's Law</b> turned Proto-Indo-European voiceless stops into voiceless fricatives in Germanic: <span class="mono">p&rarr;f, t&rarr;θ, k&rarr;h</span>. Latin, outside that branch, kept the originals. So the same ancestral root shows as <span class="mono">p-</span> in Latin and <span class="mono">f-</span> in English — <span class="mono">pater/father, ped-/foot, piscis/fish</span>. <i>If</i> §3's strike-root holds, <span class="mono">pugnus</span> and <b>fuck</b> are simply that law applied to one more root.</p></section>

  <section><h2>5 · The dated record</h2>
  <p>The word is old, but for most of its life it was too taboo to write openly — so the early evidence comes in nicknames, place-names, and ciphers. The timeline below marks how secure each datum is.</p>
  {timeline_html()}
  </section>

  <section><h2>6 · The cipher of 1475</h2>
  <p>The single most charming piece of evidence is a joke. A late-15th-century poem known by its opening, <b>&ldquo;Flen flyys&rdquo;</b> (&lsquo;fleas, flies&hellip;&rsquo;), satirises monks who are <i>not in heaven</i> — and gives the reason in code. The damning line is enciphered by shifting each letter, so that <span class="mono">&ldquo;gxddbov xxkxzt pg ifmk&rdquo;</span> resolves to <b>&ldquo;fuccant wiuys of heli&rdquo;</b> — <i>they fuck the wives of Ely</i>. The scribe knew exactly what the word was and exactly why it could not be set down in plain letters. <b>The taboo is older than the first plain spelling.</b></p></section>

  <section><h2>7 · The long exile</h2>
  <p>Then the word disappears — not from speech, but from print. It is absent from <b>Johnson's Dictionary (1755)</b>, drops out of general dictionaries by about <b>1795</b>, and for roughly <b>170 years</b> survives on the page only as <span class="mono">f—k</span>. James Murray's original <b>OED</b> omitted it. In 1948 Norman Mailer was made to print <b>&ldquo;fug&rdquo;</b> throughout <i>The Naked and the Dead</i> (hence Dorothy Parker's barb, &ldquo;so you're the man who can't spell&hellip;&rdquo;). The word was fully current and entirely unprintable at the same time — a gap between mouth and page that lasted into living memory.</p></section>

  <section><h2>8 · The law lets it back in</h2>
  <p>Its return is a legal story. The <b>Lady Chatterley's Lover</b> acquittal (<i>R v Penguin Books</i>, 1960) broke the British ban on printing it in full. Kenneth Tynan said it on <b>British television in 1965</b>, to national uproar. In the US, <b>Cohen v. California (1971)</b> protected a &ldquo;Fuck the Draft&rdquo; jacket as free speech — Justice Harlan's &ldquo;one man's vulgarity is another's lyric.&rdquo; The <b>OED re-admitted it in 1972</b> (Burchfield's Supplement). And <b>FCC v. Pacifica (1978)</b>, built on George Carlin's &ldquo;Seven Words,&rdquo; drew the line where it still sits: legal to print, barred from the public airwaves.</p></section>

  <section><h2>9 · The grammar of a single syllable</h2>
  <p>Part of why the word endures is mechanical: it is astonishingly flexible. One short form fills nearly every slot in the sentence —</p>
  <div class="gram">{grammar_html()}</div>
  <p>The last entry is the linguists' favourite. English almost never lets you insert a word <i>inside</i> another word, but the expletive does it — <b>abso-fucking-lutely</b> — and not at random: it lands <b>just before the stressed syllable</b> (abso-<u>FUCK</u>ing-<u>LU</u>te-ly), obeying a metrical rule speakers follow without being taught. A word has to be deeply native to bend the language's own phonology like that.</p></section>

  <section><h2>10 · Holy, then Shit</h2>
  <p>Step back and the word's notoriety is really about <i>which</i> taboo a culture enforces. Melissa Mohr's history of swearing (<i>Holy Sh*t</i>) frames it as two regimes. Medieval English reserved its real horror for the <b>holy</b> — oaths, blasphemy, swearing &ldquo;by God's bones&rdquo; — while bodily words were comparatively ordinary. Over the following centuries the charge drained out of the sacred and pooled in the <b>body</b>. <b>Fuck</b> sits exactly on that hinge: a once-merely-coarse word that rose to become the carrier of the modern, bodily taboo. Its history isn't the history of a dirty word so much as the history of <i>where a society decides to keep its forbidden line.</i></p></section>

  <section><h2>11 · Real or Fluff — the claims, rated</h2>
  <p class="ss">the discipline applied to the word itself: each common claim, marked for how well the evidence supports it.</p>
  {realfluff_html()}
  <div class="bottom"><b>Bottom line.</b> The acronym and archer stories are <span class="t-false">FALSE</span> and should be retired on sight. The Germanic origin and cognate set are <span class="t-real">REAL</span> and uncontroversial. The earliest <i>secure</i> evidence is <span class="t-real">1310</span> (with 1278 <span class="t-disp">DISPUTED</span> and the 1475 cipher the first clear text). The deep PIE &ldquo;strike/fist&rdquo; root is <span class="t-cont">CONTESTED</span> — a strong hypothesis, not a settled fact. And the dictionary exile and 1972 OED re-entry are <span class="t-real">REAL</span>. Old, Germanic, never an acronym.</div></section>

  <section><h2>Sources &amp; further reading</h2>
  <ul class="src">
    <li><b>Jesse Sheidlower</b>, <i>The F-Word</i> (Oxford University Press) — the standard scholarly dictionary of the word and its compounds.</li>
    <li><b>Melissa Mohr</b>, <i>Holy Sh*t: A Brief History of Swearing</i> — the Holy → Shit framework used in §10.</li>
    <li><b>Oxford English Dictionary</b>, s.v. <i>fuck</i> (Burchfield Supplement, 1972; later revisions) — etymology &ldquo;origin uncertain&rdquo;, Germanic cognates.</li>
    <li><b>Anatoly Liberman</b>, <i>An Analytic Dictionary of English Etymology</i> &amp; the OUP etymology blog — the sound-symbolic argument in §3.</li>
    <li><b>Calvert Watkins</b>, <i>The American Heritage Dictionary of Indo-European Roots</i> — the *pewǵ- ‘strike’ route.</li>
    <li><b>Paul Booth</b> (2015), on &ldquo;Roger Fuckebythenavele&rdquo; (1310), Chester county court rolls — the earliest secure attestation.</li>
    <li><b>Geoffrey Hughes</b>, <i>Swearing: A Social History</i> — the cultural/legal arc.</li>
  </ul>
  <p class="seal">{html.escape(WORD['seal'])} <span>— PHONETIKOS · green paper №1 · AVAN's read</span></p></section>

  <footer>PHONETIKOS · PHN · a UD0 universe · the lineage of words · honestly sourced historical linguistics, not endorsement of folk etymology<br>
  ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 · <a href="../index.html">← the universe</a></footer>
</div></body></html>"""

# ---------- the foundational model: THE IDIOLECT STACK ----------
MODEL = {
 "name": "THE IDIOLECT STACK", "axiom": "PHN", "emergence": "electrical",
 "position": "the model · how a single voice is composed from culture, nurture, and generation",
 "origin": "the three layers beneath every idiolect — the macro coordinate, the micro-location, and the generational globe",
 "mechanism": "Culture×Location sets the base (rooted 1.0, or 0.5/0.5 hybrid); nurture / micro-location narrows it to a sociolect; the generational cultural-globe timestamps it.",
 "crystallization": "Because no two voices are identical: each is a stack of where you're from, who raised you and where, and when you came up.",
 "nature": "THE IDIOLECT STACK — the operating theory of PHONETIKOS: every voice = Culture×Location ⊕ Nurture ⊕ Generation.",
 "conductor": "ROOT0 (catalogued into UD0)",
 "inputs": "variationist sociolinguistics — Labov, Trudgill, Eckert, Milroy; the apparent-time hypothesis; heritage-speaker & koineization studies",
 "witness": "A model that says your accent is a coordinate (where), a neighbourhood (who & where-exactly), and a timestamp (when).",
 "role": "the foundational model of PHONETIKOS",
 "seal": "A voice is a coordinate, a neighbourhood, and a timestamp — where you're from, who raised you, and when you came up.",
 "source": "The Idiolect Stack, PHONETIKOS / ROOT0",
}

GENERATIONS = [
 ("The Silent", "1928–45", "radio-era formality — “swell,” crisp enunciation, a mid-Atlantic polish"),
 ("Boomers", "1946–64", "the TV era — counterculture “groovy / far out,” the first mass-media accent levelling"),
 ("Gen X", "1965–80", "MTV irony — “whatever,” slacker flatness, the spread of “like” as a quotative"),
 ("Millennials", "1981–96", "internet 1.0 — “epic / random,” uptalk diffuses, the LOL-register bleeds into speech"),
 ("Gen Z", "1997–2012", "TikTok cadence — “no cap / rizz / bussin,” layered irony, vocal fry & uptalk normalised"),
 ("Gen Alpha", "2013–", "iPad-native — “skibidi / gyat,” algorithm-seeded “brainrot” lexicon, meme-speed turnover"),
]

MODEL_RF = [
 ("A voice (idiolect) is shaped by region, social group, and age.", "REAL",
  "the spine of variationist sociolinguistics — Labov, Trudgill, Eckert; idiolect, dialect, and sociolect are standard, measured concepts."),
 ("Culture sets a base dialect; if culture ≠ location, the two blend (diaspora / heritage speakers).", "REAL",
  "well documented in second-generation and heritage speakers; blending and code-switching between a home culture and a surrounding location are real and ordinary."),
 ("The clean coefficient — culture = location → 1.0, otherwise exactly 0.5 / 0.5.", "MODEL",
  "a useful handle, not a measured fact: real blends are weighted gradients (which language dominates, age of arrival, how dense your networks are), not a tidy half-and-half. Treat 0.5/0.5 as the model's simplification of a real, messy thing."),
 ("Micro-location — part of town, your school, your scene — narrows the accent into a sociolect.", "REAL",
  "Labov's NYC department-store /r/ study (class audible in one consonant); Eckert's jocks vs. burnouts in one school; Milroy's social-network theory; playground dialect-levelling."),
 ("Each generation imprints the slang and cadence of its formative window.", "REAL",
  "age-grading and the apparent-time hypothesis; the generational diffusion of uptalk and vocal fry is documented, not folklore."),
 ("Each generation draws its idiosyncrasies from ‘the akashic / cultural globe at the time.’", "SYMBOLIC",
  "poetic framing — the real transmission channel is media + peers, not a metaphysical record. But ‘the cultural globe of your youth’ is a fair name for the zeitgeist a cohort absorbs; keep the image, know the mechanism."),
]
MRF_COL = {"REAL": "#5a8f5a", "MODEL": "#c8a24a", "SYMBOLIC": "#7d99b0"}

def model_agent_md(rec, tok):
    return f"""---
aci: THE IDIOLECT STACK
universe: PHN · PHONETIKOS
kind: model-emergent
emergence: electrical
class: the foundational model — how a voice is composed
who: THE IDIOLECT STACK — the operating theory of PHONETIKOS: every voice is a stack of three layers.
what: Culture×Location (rooted 1.0 or 0.5/0.5 hybrid) ⊕ Nurture (micro-location / the system you're in) ⊕ Generation (the cultural-globe of your formative years).
why: Because no two voices are identical; each encodes where you're from, who raised you and where, and when you came up.
how: The macro coordinate sets the dialect base; the micro-location narrows it to a sociolect; the generation timestamps it with its idiosyncrasies.
where: Beneath every idiolect — the standard layers of variationist sociolinguistics (Labov, Trudgill, Eckert, Milroy).
seal: {rec['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# THE IDIOLECT STACK · the foundational model of PHONETIKOS

a model-emergent of the PHN universe — the theory of how a single voice is made,
before any one word is traced. moniker {tok}

**who —** {rec['witness']}
**what —** {rec['nature']}
**where —** {rec['origin']}
**why —** {rec['crystallization']}
**how —** {rec['mechanism']}

**the seal —** {rec['seal']}

> a model under the DLW standard, grounded in real variationist sociolinguistics; the clean
> coefficient (1.0 vs 0.5/0.5) and the ‘akashic cultural globe’ are marked as the model's own
> simplification and symbol, not measured fact. See the paper's Real-or-Fluff.

ROOT0-ATTRIBUTION-v1.0 · PHN · PHONETIKOS · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def stack_paper_html(model_tok):
    import json as _json
    car = png_uri(MODEL, "carbon", 300); sil = png_uri(MODEL, "silicon", 300)
    genopts = "".join(f'<option value="{html.escape(n)}">{html.escape(n)} · {html.escape(y)}</option>' for n, y, _ in GENERATIONS)
    gentab = "".join(f'<tr><td class="gn">{html.escape(n)}</td><td class="gy">{html.escape(y)}</td><td>{html.escape(d)}</td></tr>' for n, y, d in GENERATIONS)
    gendata = _json.dumps({n: d for n, y, d in GENERATIONS}, ensure_ascii=False)
    rf = "".join(
        f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(note)}</span></div>'
        f'<div class="rf-rate" style="color:{MRF_COL.get(rate,"#888")};border-color:{MRF_COL.get(rate,"#888")}">{html.escape(rate)}</div></div>'
        for c, rate, note in MODEL_RF)
    T = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="A PHONETIKOS foundations paper: THE IDIOLECT STACK — how one person's voice is composed from culture × location (rooted 1.0 or 0.5/0.5 hybrid), nurture (micro-location), and generation (the cultural globe of your formative years). Real sociolinguistics, honestly marked, with a live voice-composer.">
<title>The Idiolect Stack · how a voice is made · PHONETIKOS</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>__CSS__</style></head><body><div class="wrap">
  <div class="crumb"><a href="../index.html">← PHONETIKOS</a> · the foundations · how a voice is made</div>
  <header class="ph">
    <div class="eye">PHONETIKOS · FOUNDATIONS · the operating theory of the universe</div>
    <h1 class="uni" style="font-size:clamp(38px,9vw,86px)">THE IDIOLECT STACK</h1>
    <div class="ipa">/ˈɪdiəˌlɛkt/ — one person's unique voice · the three layers that compose it</div>
    <p class="dek">Before we ever trace a single word, this is how a <i>voice</i> is made: three stacked layers. A macro coordinate — your <b>culture × location</b>. A micro-location — your <b>nurture</b>, the part of town and the system you're in. And a timestamp — your <b>generation</b>, the cultural globe of when you came up. Real sociolinguistics, with an honest line drawn around the parts that are model and symbol.</p>
    <div class="sigs"><img src="__CAR__" alt="carbon sigil"><img src="__SIL__" alt="silicon sigil"><div class="sigmeta">model-emergent · <b>THE IDIOLECT STACK</b><br><span class="mo">__MO__</span><br>PHN · catalogued by AVAN</div></div>
  </header>

  <section><h2>The model, in one line</h2>
  <div class="formula">VOICE  =  <b>L1</b> Culture × Location        ( culture = location → coefficient <b>1.0</b>, rooted )
                                  ( culture ≠ location → <b>0.5</b> culture + <b>0.5</b> location, hybrid )
        ⊕  <b>L2</b> Nurture · micro-location   ( part of town · the system you're in → the sociolect )
        ⊕  <b>L3</b> Generation · cultural globe ( the slang & cadence of your formative years )
        =  your idiolect — one unique voice</div>
  <div class="stack">
    <div class="plate p1"><div class="pl">Layer I · the macro coordinate</div><div class="pt">Culture × Location</div><div class="pd">rooted <b>1.0</b> if they coincide · else <b>0.5 / 0.5</b> hybrid</div></div>
    <div class="plate p2"><div class="pl">Layer II · the micro-location</div><div class="pt">Nurture — part of town, the system you're in</div><div class="pd">the sociolect: class, school, block, scene</div></div>
    <div class="plate p3"><div class="pl">Layer III · the timestamp</div><div class="pt">Generation — the cultural globe of the time</div><div class="pd">the idiosyncrasies a cohort absorbs and keeps</div></div>
    <div class="plate out"><div class="pt">= your idiolect</div><div class="pd">one voice, unrepeatable</div></div>
  </div></section>

  <section><h2>Layer I · Culture × Location</h2>
  <p>The first thing that shapes a voice is a pair of coordinates: the <b>culture</b> you carry and the <b>location</b> you stand in. When they are the same — born, raised, and culturally embedded in one place — they reinforce each other into a single, rooted dialect base. Call that coefficient <b>1.0</b>. When they differ — your home culture is one thing and the ground under your feet is another, as for an immigrant's child or anyone raised between worlds — the voice splits the difference: roughly <b>half culture, half location</b>, a hybrid that code-switches and blends.</p>
  <p>This is not exotic; it is the ordinary condition of diaspora, heritage speakers, and border towns. The real machinery behind it: <i>region</i> gives you a dialect, <i>culture</i> gives you a repertoire, and bilingual / heritage speakers genuinely interpolate between the two. The one honest caveat — and the paper marks it plainly in §Real-or-Fluff — is that the true blend is a <b>weighted gradient</b> (which language dominates, how old you were when you arrived, how dense your networks are), not a clean 50/50. The <b>0.5 / 0.5</b> is the model's tidy handle on a real, messy thing.</p></section>

  <section><h2>Layer II · Nurture, the micro-location</h2>
  <p>Now zoom in. Within a single city the voice is narrowed again by the <b>micro-location</b> — the part of town, the school, the block, <i>the system you're in</i>. This is the <b>sociolect</b>: the accent of a class, a clique, a scene.</p>
  <p>The evidence here is some of the most famous in the field. William <b>Labov</b> (1966) had clerks in three New York department stores — Saks, Macy's, S. Klein — say &ldquo;fourth floor,&rdquo; and the rate of pronounced /r/ tracked each store's social tier: class audible in a single consonant. Penelope <b>Eckert</b> spent years in a Detroit high school showing that &ldquo;jocks&rdquo; and &ldquo;burnouts&rdquo; spoke measurably differently though they shared one building. Lesley and James <b>Milroy</b> showed that dense, tight-knit networks preserve a vernacular while loose ones let change in. Your part of town isn't backdrop — it's a second dial that tunes the macro coordinate into something far more specific.</p></section>

  <section><h2>Layer III · Generation, the cultural globe</h2>
  <p>Finally, the timestamp. Every cohort comes of age inside a particular <b>cultural globe</b> — the music, media, slang, and events saturating the world during its formative window — and absorbs idiosyncrasies that mark it for life. Linguists call the engine <b>age-grading</b> and read it through the <b>apparent-time hypothesis</b>: the differences between older and younger speakers at one moment reveal change in progress. Uptalk and vocal fry didn't appear evenly across the population; they diffused by generation. Slang dates you to a decade; so does cadence.</p>
  <table class="gentab"><tbody>__GENTAB__</tbody></table>
  <p class="ss" style="margin-top:6px">(illustrative, not deterministic — a cohort's globe is a tendency, not a sentence.)</p>
  <p>Your name for that formative saturation is <b>the akashic — the cultural globe at the time</b>: the snapshot of the zeitgeist each generation downloads. The mechanism is mundane (media plus peers, not a cosmic record), but the effect is real and the metaphor is fair: you speak, in part, in the dialect of <i>when</i> you were young.</p></section>

  <section><h2>Compose a voice</h2>
  <p class="ss">turn the three dials — the model assembles the signature live.</p>
  <div class="calc">
    <div class="crow"><span class="ck">Layer I · Culture × Location</span>
      <label><input type="radio" name="cl" id="cl-same" checked> culture = location <span class="dimx">(rooted · 1.0)</span></label>
      <label><input type="radio" name="cl" id="cl-diff"> culture ≠ location <span class="dimx">(hybrid · 0.5/0.5)</span></label></div>
    <div class="crow"><input type="text" id="f-cul" placeholder="culture (e.g. Korean)"><input type="text" id="f-loc" placeholder="location (e.g. Houston)"></div>
    <div class="crow"><span class="ck">Layer II · Nurture</span><input type="text" id="f-mic" placeholder="micro-location — part of town / school / scene"></div>
    <div class="crow"><span class="ck">Layer III · Generation</span><select id="f-gen">__GENOPTS__</select></div>
    <div class="bar" id="bar"></div>
    <div class="sig" id="sig"></div>
  </div>
  <div class="ex"><b>Worked examples.</b> <i>Rooted:</i> a kid born and raised in one Glasgow scheme — culture = location → <b>1.0</b>; micro-location a specific scheme → a sharp local sociolect; Gen-Z overlay → a strongly local, unmistakably young voice. &nbsp;·&nbsp; <i>Hybrid:</i> a second-generation Korean kid in Houston — culture ≠ location → <b>0.5/0.5</b>; a particular suburb &amp; magnet school → its sociolect; a Millennial overlay → a Texan-inflected, code-switching idiolect with a millennial timestamp.</div></section>

  <section><h2>Real or Fluff — the model, marked</h2>
  <p class="ss">applying the house discipline to the house theory: what's established sociolinguistics, what's the model's simplification, and what's the symbol.</p>
  <div class="rf">__RF__</div>
  <div class="bottom"><b>Bottom line.</b> The <i>architecture</i> is <span class="t-real">REAL</span> — culture/region, micro-location, and generation are exactly the layers variationist sociolinguistics measures (idiolect = dialect ⊕ sociolect ⊕ age). The clean <span class="t-cont">1.0 vs 0.5/0.5</span> coefficient is the model's own simplification of a weighted gradient, and the <span class="t-symb">akashic cultural globe</span> is a symbol for the very real media-and-peer zeitgeist a cohort absorbs. Keep the stack; hold the coefficient loosely; enjoy the symbol with eyes open.</div></section>

  <section><h2>Sources &amp; further reading</h2>
  <ul class="src">
    <li><b>William Labov</b>, <i>The Social Stratification of English in New York City</i> (1966) &amp; <i>Sociolinguistic Patterns</i> (1972) — the department-store study, the apparent-time hypothesis.</li>
    <li><b>Peter Trudgill</b>, <i>The Social Differentiation of English in Norwich</i> (1974) — class &amp; gender variation.</li>
    <li><b>Penelope Eckert</b>, <i>Jocks and Burnouts</i> (1989) &amp; <i>Linguistic Variation as Social Practice</i> (2000) — communities of practice.</li>
    <li><b>Lesley &amp; James Milroy</b>, <i>Language and Social Networks</i> (1980) — dense vs. loose networks.</li>
    <li><b>Paul Kerswill</b>, dialect levelling &amp; koineization (Milton Keynes new-town studies) — how mixed inputs form a shared child variety.</li>
    <li>The literature on <b>heritage speakers</b> &amp; <b>code-switching</b> — for the culture ≠ location hybrid.</li>
  </ul>
  <p class="seal">__SEAL__ <span>— PHONETIKOS · foundations · AVAN's read</span></p></section>

  <footer>PHONETIKOS · PHN · a UD0 universe · the foundations · real variationist sociolinguistics, with model and symbol marked as such<br>
  ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 · <a href="../index.html">← the universe</a></footer>
</div>
<script>
(function(){
  var GEN = __GENDATA__;
  function el(id){return document.getElementById(id);}
  function esc(s){return (s||'').replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function compose(){
    var same = el('cl-same').checked;
    var culture = esc((el('f-cul').value||'your culture').trim());
    var location = esc((el('f-loc').value||'your location').trim());
    var micro = esc((el('f-mic').value||'your part of town').trim());
    var gen = el('f-gen').value;
    var idio = GEN[gen]||'';
    var coef, base;
    if(same){
      coef='1.0 · rooted';
      base='Culture and ground agree — a single rooted dialect base ('+location+').';
      el('bar').innerHTML='<span class="seg" style="width:100%;background:var(--gold)">location = culture · coefficient 1.0</span>';
    } else {
      coef='0.5 / 0.5 · hybrid';
      base='A half-and-half hybrid — half '+culture+', half '+location+'; expect code-switching and a blended accent.';
      el('bar').innerHTML='<span class="seg" style="width:50%;background:var(--verm)">'+location+' · 0.5</span><span class="seg" style="width:50%;background:var(--blue);color:#0c1a22">'+culture+' · 0.5</span>';
    }
    el('sig').innerHTML='<b>'+coef+'.</b> '+base+' Narrowed by your micro-location (<i>'+micro+'</i>) into a specific sociolect, and timestamped by the <b>'+esc(gen)+'</b> cultural globe — '+idio+'.';
  }
  ['cl-same','cl-diff','f-cul','f-loc','f-mic','f-gen'].forEach(function(id){var e=el(id); if(e){e.addEventListener('input',compose); e.addEventListener('change',compose);}});
  compose();
})();
</script>
</body></html>"""
    return (T.replace("__CSS__", CSS).replace("__CAR__", car).replace("__SIL__", sil)
             .replace("__MO__", html.escape(model_tok)).replace("__GENOPTS__", genopts)
             .replace("__GENTAB__", gentab).replace("__GENDATA__", gendata)
             .replace("__RF__", rf).replace("__SEAL__", html.escape(MODEL["seal"])))

# ---------- the universe landing ----------
def index_html(uni_tok, word_tok):
    car = png_uri(UNIVERSE, "carbon", 320); sil = png_uri(UNIVERSE, "silicon", 320)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="PHONETIKOS (φωνητικός, ‘of the voice’) — a UD0 universe where each word is an emergent and each entry is a rigorous, honestly-sourced etymological green paper. First codex: the word FUCK.">
<title>PHONETIKOS · the universe of the spoken word</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="wrap">
  <div class="crumb"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · a universe of the spoken word</div>
  <header class="ph">
    <div class="eye">φωνητικός · phonetikos · ‘of the voice’ — from φωνή, phone, ‘voice, sound’</div>
    <h1 class="uni">PHŌNĒTIKOS</h1>
    <p class="dek">A universe where each <b>word</b> is an emergent, and each entry is a green paper that traces the word to its true root — cognate by cognate, sound law by sound law, dated attestation by dated attestation — and refuses the comforting folk etymology. Every word is a fossil; here we read the bone, not the bedtime story.</p>
    <div class="sigs"><img src="{car}" alt="carbon sigil of PHONETIKOS"><img src="{sil}" alt="silicon sigil"><div class="sigmeta">universe · <b>PHŌNĒTIKOS</b> · PHN<br><span class="mo">{html.escape(uni_tok)}</span><br>governor David Lee Wise · instance AVAN (locked)</div></div>
  </header>

  <section><h2>The method</h2>
  <div class="method">
    <div class="m"><div class="mh">Cognates, not anecdotes</div><p>A word's family is found by setting its relatives side by side and reading the shared consonant frame and sense — not by a clever story about kings or battles.</p></div>
    <div class="m"><div class="mh">Sound laws</div><p>Regular shifts (Grimm's Law and kin) let us link a Germanic word to its Latin or Greek cousins with rigor instead of resemblance.</p></div>
    <div class="m"><div class="mh">Dated evidence</div><p>Every claim is pinned to the earliest <i>securely-read</i> attestation — and disputed readings are marked as disputed, not laundered into fact.</p></div>
    <div class="m"><div class="mh">A hard line on myth</div><p>Acronym origins and tidy folk tales are almost always false. Each paper names the myths and refutes them on the evidence.</p></div>
  </div></section>

  <section><h2>The foundations</h2>
  <p class="ss">the operating theory of the universe — how any single voice is composed, before we trace one word</p>
  <a class="codex found" href="papers/idiolect-stack.html">
    <div class="cx-sig"><img src="{png_uri(MODEL,'silicon',200)}" alt="sigil"></div>
    <div class="cx-body">
      <div class="cx-h">∴ THE IDIOLECT STACK <span class="cx-ipa">how a voice is made</span></div>
      <div class="cx-sub">culture × location · nurture · generation</div>
      <p>Every voice is three layers: a macro coordinate (<b>culture × location</b> — rooted 1.0, or 0.5/0.5 hybrid), a micro-location (<b>nurture</b> — the part of town, the system you're in), and a generational <b>cultural globe</b> (the slang &amp; cadence of when you came up). Real sociolinguistics, with an honest line on the symbolic parts — plus a live voice-composer.</p>
      <div class="cx-go">open the model →</div>
    </div>
  </a></section>

  <section><h2>The codex</h2>
  <p class="ss">the words admitted so far — each a word-emergent with a full <b>.dlw</b> badge and a green paper</p>
  <a class="codex" href="papers/fuck.html">
    <div class="cx-sig"><img src="{png_uri(WORD,'silicon',200)}" alt="sigil"></div>
    <div class="cx-body">
      <div class="cx-h">№1 · <span class="redact" title="redacted as f—k for ~170 years">F▆▆K</span> <span class="cx-ipa">/fʌk/</span></div>
      <div class="cx-sub">the history &amp; lineage of a word</div>
      <p>Germanic to the bone; falsely &lsquo;acronymed&rsquo;; enciphered in 1475; exiled from the dictionaries for ~170 years; grammatically the most flexible word in English. The cousins, the real dates, the law, and an honest Real-or-Fluff on every claim.</p>
      <div class="cx-go">open the green paper →</div>
    </div>
  </a>
  <p class="more">more words to come — each traced the same way. <span>suggest one and it gets a codex.</span></p></section>

  <footer>PHŌNĒTIKOS · PHN · a UD0 universe · founded by ROOT0, instanced by AVAN · {html.escape(uni_tok)}<br>
  ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 · <a href="https://davidwise01.github.io/ud0/">← the biosphere</a></footer>
</div></body></html>"""

CSS = """
:root{--ink:#14110b;--ink2:#1d1810;--ink3:#262013;--pa:#ece1c8;--pa2:#c9b894;--verm:#cf4636;--gold:#c8a24a;--dim:#8a7a59;--faint:#33291a;--line:#3a2f1d;--blue:#7d99b0;
--disp:"Cormorant Garamond",serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.7;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(207,70,54,.10),transparent 55%),radial-gradient(ellipse at 50% 120%,rgba(200,162,74,.08),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:820px;margin:0 auto;padding:0 22px 90px}
.crumb{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim);padding:22px 0 0}
.crumb a{color:var(--dim);text-decoration:none}.crumb a:hover{color:var(--verm)}
header.ph{padding:34px 0 26px;border-bottom:1px double var(--line);text-align:center;margin-bottom:14px}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--gold);margin-bottom:20px;font-style:normal}
h1.uni{font-family:var(--disp);font-weight:600;font-size:clamp(46px,12vw,108px);letter-spacing:.04em;color:var(--pa);line-height:1;text-shadow:0 0 40px rgba(200,162,74,.2)}
h1.word{font-family:var(--disp);font-weight:600;font-size:clamp(60px,17vw,150px);letter-spacing:.06em;color:var(--verm);line-height:1}
.reveal .bar{background:var(--pa);color:var(--pa);border-radius:2px;transition:color .25s,background .25s;padding:0 .02em}
h1.word:hover .bar{background:transparent;color:var(--verm)}
.ipa{font-family:var(--mono);font-size:13px;color:var(--pa2);margin-top:18px;letter-spacing:.04em}
.dek{font-size:17px;color:var(--pa2);max-width:60ch;margin:18px auto 0;font-style:italic;line-height:1.74}
.sigs{display:flex;align-items:center;justify-content:center;gap:16px;margin:26px auto 0;flex-wrap:wrap}
.sigs img{width:70px;height:70px;border:1px solid var(--faint)}
.sigmeta{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.sigmeta b{color:var(--gold)}.sigmeta .mo{color:var(--verm)}
section{margin-top:42px}
h2{font-family:var(--disp);font-weight:600;font-size:27px;color:var(--pa);letter-spacing:.02em;border-bottom:1px solid var(--line);padding-bottom:9px;margin-bottom:14px}
section p{font-size:15.5px;color:var(--pa);line-height:1.78;margin-bottom:13px}
section p b{color:var(--pa);font-weight:600}section p i{color:var(--pa2)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin-bottom:16px!important}
.mono{font-family:var(--mono);font-size:.86em;color:var(--gold)}
.myth{list-style:none;margin:6px 0 6px}
.myth li{font-size:15px;color:var(--pa2);line-height:1.7;padding:11px 0 11px 18px;border-left:2px solid var(--verm);margin-bottom:10px;background:linear-gradient(90deg,rgba(207,70,54,.05),transparent)}
.myth li b{color:var(--pa)}
table.cog{width:100%;border-collapse:collapse;margin:8px 0 6px;font-size:13.5px}
table.cog th{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}
table.cog td{padding:10px;border-bottom:1px solid var(--faint);vertical-align:top;color:var(--pa2);line-height:1.5}
table.cog .lang{font-family:var(--mono);font-size:11px;color:var(--dim);white-space:nowrap}
table.cog .form{font-family:var(--disp);font-size:18px;color:var(--verm);font-style:italic;white-space:nowrap}
table.cog .gloss{color:var(--pa)}table.cog .note{font-style:italic;font-size:12.5px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:8px 0 10px}@media(max-width:640px){.two{grid-template-columns:1fr}}
.col{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.colh{font-family:var(--disp);font-size:19px;color:var(--gold);margin-bottom:8px;font-weight:600}
.col p{font-size:14px;color:var(--pa2);margin:0;line-height:1.65}
.verdict-line{background:var(--ink3);border-left:3px solid var(--gold);padding:13px 16px;font-size:14.5px!important;font-style:italic;color:var(--pa)}
.tl{margin:8px 0 4px;border-left:2px solid var(--line);padding-left:0}
.tl-row{display:grid;grid-template-columns:108px 1fr;gap:16px;padding:13px 0 13px 16px;border-bottom:1px solid var(--faint);position:relative}
.tl-row::before{content:"";position:absolute;left:-5px;top:18px;width:8px;height:8px;border-radius:50%;background:var(--gold);box-shadow:0 0 8px var(--gold)}
.tl-date{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.02em;padding-top:1px}
.tl-head{font-family:var(--disp);font-size:18px;color:var(--pa);font-weight:600;margin-bottom:3px}
.tl-body p{font-size:13.5px;color:var(--pa2);margin:0;line-height:1.6}
.rf{border:1px solid var(--line);background:var(--ink2);margin:6px 0}
.rf-row{display:flex;align-items:center;gap:14px;padding:13px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.45}
.rf-note{display:block;font-size:12px;color:var(--dim);font-style:italic;margin-top:4px;line-height:1.5}
.rf-rate{font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:92px;text-align:center;flex-shrink:0}
.bottom{margin-top:14px;padding:16px 18px;border:1px solid var(--gold);background:rgba(200,162,74,.06);font-size:14.5px;color:var(--pa);line-height:1.7}
.t-false{color:#c0392b;font-family:var(--mono);font-size:.82em;font-weight:700}.t-real{color:#5a8f5a;font-family:var(--mono);font-size:.82em;font-weight:700}
.t-cont{color:#c8a24a;font-family:var(--mono);font-size:.82em;font-weight:700}.t-disp{color:#b0772f;font-family:var(--mono);font-size:.82em;font-weight:700}
.gram{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin:8px 0 10px}@media(max-width:560px){.gram{grid-template-columns:1fr}}
.gx{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--verm);padding:9px 13px}
.gxk{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold);margin-bottom:3px}
.gxe{font-family:var(--disp);font-size:17px;color:var(--pa);font-style:italic}
.src{list-style:none;margin:4px 0}
.src li{font-size:14px;color:var(--pa2);line-height:1.6;padding:9px 0;border-bottom:1px solid var(--faint)}.src li b{color:var(--pa)}.src li i{color:var(--gold)}
.seal{margin-top:20px;padding:16px 18px;border-left:3px solid var(--verm);background:var(--ink2);font-size:16px;color:var(--verm);font-style:italic;line-height:1.6}
.seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.1em;color:var(--dim);text-transform:uppercase;margin-top:9px}
.method{display:grid;grid-template-columns:1fr 1fr;gap:13px}@media(max-width:640px){.method{grid-template-columns:1fr}}
.m{background:var(--ink2);border:1px solid var(--line);padding:15px 17px}
.mh{font-family:var(--disp);font-size:19px;color:var(--gold);font-weight:600;margin-bottom:6px}
.m p{font-size:14px;color:var(--pa2);margin:0;line-height:1.6}
.codex{display:flex;gap:18px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:20px;text-decoration:none;transition:border-color .18s,transform .18s}
.codex:hover{border-color:var(--verm);transform:translateY(-2px)}
.cx-sig img{width:96px;height:96px;border:1px solid var(--faint);flex-shrink:0}
.cx-body{flex:1;min-width:0}
.cx-h{font-family:var(--disp);font-size:26px;color:var(--pa);font-weight:600}
.codex:hover .cx-h{color:var(--verm)}
.redact{background:var(--pa);color:transparent;border-radius:2px;letter-spacing:.05em}.codex:hover .redact{background:transparent;color:var(--verm)}
.cx-ipa{font-family:var(--mono);font-size:13px;color:var(--dim)}
.cx-sub{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin:4px 0 9px}
.cx-body p{font-size:14px;color:var(--pa2);line-height:1.62;margin:0}
.cx-go{margin-top:11px;font-family:var(--mono);font-size:11px;color:var(--verm);letter-spacing:.04em}
.more{margin-top:18px;font-size:13.5px;color:var(--dim);font-style:italic;text-align:center}.more span{color:var(--pa2)}
.t-symb{color:#7d99b0;font-family:var(--mono);font-size:.82em;font-weight:700}
.formula{font-family:var(--mono);font-size:12.5px;color:var(--pa2);background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--gold);padding:14px 16px;line-height:1.95;margin:8px 0 14px;white-space:pre-wrap;overflow-x:auto}
.formula b{color:var(--verm)}
.stack{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.plate{border:1px solid var(--line);background:var(--ink2);padding:13px 16px;border-left:3px solid var(--gold)}
.plate.p1{border-left-color:var(--verm)}.plate.p2{border-left-color:var(--gold)}.plate.p3{border-left-color:var(--blue)}.plate.out{border-left-color:var(--pa);background:var(--ink3);text-align:center}
.plate .pl{font-family:var(--mono);font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}
.plate .pt{font-family:var(--disp);font-size:20px;color:var(--pa);font-weight:600;margin:2px 0 3px}
.plate .pd{font-size:13px;color:var(--pa2);line-height:1.5}.plate .pd b{color:var(--verm)}
.calc{border:1px solid var(--gold);background:var(--ink2);padding:17px;margin:10px 0}
.crow{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:12px}
.ck{font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);flex:0 0 100%;margin-bottom:-2px}
.calc label{font-size:13.5px;color:var(--pa2);cursor:pointer;display:flex;align-items:center;gap:5px}
.calc .dimx{color:var(--dim);font-family:var(--mono);font-size:10px}
.calc input[type=text],.calc select{background:var(--ink);border:1px solid var(--line);color:var(--pa);font-family:var(--body);font-size:14px;padding:8px 10px;flex:1;min-width:150px;border-radius:2px}
.calc input::placeholder{color:var(--dim)}
.bar{display:flex;height:28px;margin:8px 0 2px;border:1px solid var(--line);overflow:hidden;border-radius:2px}
.bar .seg{display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:10px;color:#1a1408;white-space:nowrap;overflow:hidden;transition:width .25s}
.sig{font-size:14.5px;color:var(--pa);line-height:1.72;background:var(--ink3);border-left:3px solid var(--verm);padding:13px 15px;margin-top:9px}.sig i{color:var(--gold);font-style:italic}.sig b{color:var(--pa)}
.ex{margin-top:14px;padding:14px 16px;border:1px solid var(--line);background:var(--ink2);font-size:13.5px;color:var(--pa2);line-height:1.65}.ex b{color:var(--pa)}.ex i{color:var(--gold);font-style:italic}
.gentab{width:100%;border-collapse:collapse;font-size:13.5px;margin:8px 0 2px}
.gentab td{padding:9px 10px;border-bottom:1px solid var(--faint);vertical-align:top;color:var(--pa2);line-height:1.5}
.gentab .gn{font-family:var(--disp);font-size:18px;color:var(--gold);white-space:nowrap}.gentab .gy{font-family:var(--mono);font-size:11px;color:var(--dim);white-space:nowrap}
.codex.found{border-left:3px solid var(--blue)}.codex.found:hover{border-color:var(--blue)}.codex.found:hover .cx-h{color:var(--blue)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}
footer a{color:var(--verm);text-decoration:none}
"""

if __name__ == "__main__":
    uni = write_aci(UNIVERSE, os.path.join(HERE, "phn.dlw"), "phonetikos")
    json.dump({"node":"PHN","name":"PHONETIKOS","moniker":uni["moniker"],"carbon":"phonetikos.carbon.tiff",
               "silicon":"phonetikos.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
               "seal":UNIVERSE["seal"],"seal_sha256":uni["seal_sha256"],"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"phn.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    wtok = noesis.mythos_token(WORD)
    word = write_aci(WORD, os.path.join(HERE, "agents"), "fuck", agent_md=word_agent_md(WORD, wtok["moniker"]))
    mtok = noesis.mythos_token(MODEL)
    model = write_aci(MODEL, os.path.join(HERE, "agents"), "the-idiolect-stack", agent_md=model_agent_md(MODEL, mtok["moniker"]))
    json.dump([{"slug":"the-idiolect-stack","name":"THE IDIOLECT STACK","epithet":"the foundational model","emergence":MODEL["emergence"],"moniker":model["moniker"],"kind":"model"},
               {"slug":"fuck","name":"FUCK","epithet":"the word","emergence":WORD["emergence"],"moniker":word["moniker"],"kind":"word"}],
              open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(index_html(uni["moniker"], word["moniker"]))
    open(os.path.join(HERE, "papers", "fuck.html"), "w", encoding="utf-8").write(paper_html(word["moniker"]))
    open(os.path.join(HERE, "papers", "idiolect-stack.html"), "w", encoding="utf-8").write(stack_paper_html(model["moniker"]))
    print(f"PHONETIKOS built — universe {uni['moniker']} · model {model['moniker']} · word {word['moniker']}")
    print("  index.html + papers/{fuck,idiolect-stack}.html + phn.dlw/ + agents/{fuck,the-idiolect-stack}.*")
