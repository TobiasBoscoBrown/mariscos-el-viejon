# -*- coding: utf-8 -*-
import os, html, json
OUT="/tmp/site"
PHONE="(208) 910-9471"; TEL="2089109471"
ADDR="1125 Caldwell Blvd, Nampa, ID 83651"
NAME="Mariscos El Viejon"
MAPS="https://www.google.com/maps/place/MARISCOS+EL+VIEJON/@43.5999975,-116.5956566,17z/data=!3m1!4b1!4m6!3m5!1s0x54ae4d1fe7099793:0x9c2d94a673b8a7d1!8m2!3d43.5999975!4d-116.5956566!16s%2Fg%2F11j2_yd3s5"
SITE="https://mariscos-el-viejon.vercel.app"
RATING="4.5"; RCOUNT="668"

HOURS=[("Monday","11 AM to 9 PM"),("Tuesday","Closed"),("Wednesday","11 AM to 9 PM"),
("Thursday","11 AM to 9 PM"),("Friday","11 AM to 9:30 PM"),("Saturday","11 AM to 9:30 PM"),("Sunday","11 AM to 9 PM")]

# ---- Reviews (real, verbatim, attributed, Google) ----
REVIEWS=[
 ("BAI H","2 months ago",5,"The service is really good, I had a big ole Pacifico and a plate of all three ceviches and it exceeded my expectations."),
 ("Rick Youra","3 months ago",5,"This is our new favorite place! We have gone twice this week and both times Richard guided us through the menu and extended us excellent service. We will definitely be back to work our way through the menu."),
 ("Armando Rodriguez","5 months ago",5,"Amazing service and atmosphere! I love to come here after work hours at the bar or with my family on a weekend. The food is excellent and the service is amazing. Highly recommended!"),
 ("Mrs. H Av","a year ago",5,"I am impressed by how clean El Viejon is! Normally, seafood restaurants have that unpleasant smell; not here! I recommend the ceviche. It is fresh, full of flavor, with a hint of sweetness."),
 ("Lisa Schaefer","a year ago",5,"Their menu is filled with many options. And they have a bar, not just beers! Waitress was great, she kept checking on us."),
 ("Mary Panzer","2 years ago",5,"My husband likes seafood, so I thought we would try this place. The food was good, and very generous. They did interesting things with food that we had never had before. We split a ceviche tower. Very clever and plenty for two."),
 ("Annie Lane","8 months ago",4,"Great place to eat and enjoy the food. Can sit outside if you want, has a full bar. On the weekend plenty of families, with plenty of children. Some singing, all types of people there enjoying the time out."),
 ("Liah","7 months ago",5,"Amazing food! Amazing customer service, fun atmosphere! I couldn't say enough good things about this restaurant. Definitely a new favorite spot!"),
]

# ---- Menu categories (each its own page) ----
# fields: slug, name, tag, hero img, blurb, good_for, includes, items[(name,desc,price)]
CATS=[
{"slug":"ceviches-aguachiles","name":"Ceviches y Aguachiles","tag":"Bright, citrus-cured, ice cold",
 "img":"aguachile.jpg","alt":"Aguachile verde de camaron at Mariscos El Viejon",
 "blurb":"Shrimp and fish cured in lime and chile, served cold and bright. This is where regulars start, and it is the dish reviewers name most often for being fresh and clean.",
 "good_for":"A light, sharable start, hot summer days, anyone who loves citrus and a little heat",
 "howlong":"Made to order, comes out cold and fresh",
 "includes":"Saltines or tostadas, lime, salsas, and cucumber on the side",
 "items":[("Aguachile Verde de Camaron","Raw shrimp swimming in a bright green lime and serrano sauce with cucumber and red onion.",""),
          ("Ceviche de Camaron","Chopped shrimp cured in lime with tomato, onion, cilantro and avocado.",""),
          ("Tostada de Ceviche","A crisp tostada piled with ceviche and topped with avocado.",""),
          ("Aguachile Negro","Shrimp in a dark chile and citrus sauce for a deeper, smokier heat.","")]},
{"slug":"cocteles-torres","name":"Cocteles y Torres de Mariscos","tag":"The showpiece seafood",
 "img":"torre-mariscos.jpg","alt":"Torre de mariscos seafood tower at Mariscos El Viejon",
 "blurb":"Cold shrimp cocktails loaded to the rim, and the Torre de Mariscos, the seafood tower everyone photographs. One couple said they split the tower and it was plenty for two.",
 "good_for":"Sharing with a group, a celebration, seafood lovers who want the full spread",
 "howlong":"Built fresh, the tower takes a few extra minutes",
 "includes":"Saltines, tostadas, lime and house salsas",
 "items":[("Torre de Mariscos","The signature tower. Layers of shrimp, octopus, fish and avocado stacked in a tall glass.",""),
          ("Coctel de Camaron","Cold shrimp cocktail in a tangy tomato and clamato base with avocado and cilantro.",""),
          ("Campechana","A mixed cocktail of shrimp, octopus and more in a chilled house sauce.",""),
          ("Molcajete de Mariscos","A bubbling stone molcajete loaded with mixed seafood.",""),
          ("Botana El Viejon","A large mixed seafood platter built for the table.","")]},
{"slug":"tacos-birria-fajitas","name":"Tacos, Birria y Fajitas","tag":"Off the grill and the comal",
 "img":"birria-tacos.jpg","alt":"Quesabirria tacos with consome at Mariscos El Viejon",
 "blurb":"Quesabirria with consome for dipping, tacos de asada off the grill, and sizzling fajitas. The non seafood lineup that keeps everyone at the table happy.",
 "good_for":"Anyone who is not in the mood for seafood, hearty appetites, dipping fans",
 "howlong":"Cooked to order on the grill and comal",
 "includes":"Consome for the birria, onion, cilantro, lime and salsas",
 "items":[("Quesabirria","Birria and melted cheese in a griddled tortilla, served with a cup of rich consome for dipping.",""),
          ("Tacos de Asada","Grilled steak tacos on warm tortillas with onion and cilantro.",""),
          ("Fajita Asada","A sizzling skillet of grilled steak with peppers and onions.",""),
          ("Sopes","Thick masa sopes topped with your choice of chicken, asada or birria.","3.75 each")]},
{"slug":"caldos-sopas","name":"Caldos y Sopas","tag":"Hot bowls, big comfort",
 "img":"caldo-mariscos.jpg","alt":"Caldo de mariscos seafood soup at Mariscos El Viejon",
 "blurb":"Big steaming bowls of seafood soup that regulars swear by, especially on a cool Idaho evening. Loaded with shrimp and fresh fish.",
 "good_for":"A cold day, a hearty single dish, anyone feeling a little under the weather",
 "howlong":"Served hot in a generous bowl",
 "includes":"Rice, lime, onion, cilantro and warm tortillas",
 "items":[("Caldo de Mariscos (Siete Mares)","A seven seas seafood soup loaded with shrimp, fish and more in a rich broth.",""),
          ("Caldo de Camaron","A hearty shrimp soup in a deep, savory broth.",""),
          ("Menudo","Traditional weekend menudo, simmered slow.","")]},
{"slug":"platillos-mexicanos","name":"Platillos Mexicanos","tag":"Burritos, quesadillas y mas",
 "img":"tacos-asada.jpg","alt":"Tacos de asada plate at Mariscos El Viejon",
 "blurb":"The full Mexican comfort lineup with real prices, from wet burritos to quesadillas and chimichangas. Bring someone who is not into seafood and they are covered.",
 "good_for":"Familiar favorites, lunch, picky eaters and big appetites",
 "howlong":"Made to order, most plates come with rice and beans",
 "includes":"Rice and beans where noted, chips and salsa with one free refill",
 "items":[("Burrito Regular","Choice of meat with rice, beans and cheese. Chicken or asada.","Chicken 9.00 / Asada 11.00"),
          ("Wet Burrito","Smothered burrito with sauce and melted cheese.","Chicken 10.99 / Steak 12.99"),
          ("Quesadilla","Flour tortilla with the meat of your choice, served with rice and beans.","Chicken 9.00 / Asada 11.99 / Camaron 14.99"),
          ("Chimichanga","Choice of meat with cheese and salad.","Chicken 9.99 / Steak 11.50"),
          ("Enchiladas Rojas","Red sauce enchiladas, a house comfort plate.","12.99"),
          ("Orden de Flautas","Crisp rolled flautas, an order to share.","11.99")]},
{"slug":"cantina-micheladas","name":"Cantina, Cervezas y Micheladas","tag":"A full bar, not just beer",
 "img":"michelada.jpg","alt":"Michelada at the Mariscos El Viejon cantina",
 "blurb":"This is a full cantina. Micheladas built tall, margaritas, a long draft and import list, and five dollar tequila on Thursdays. Reviewers love that it is a bar and not just beers.",
 "good_for":"Happy hour, weekend nights with live music, pairing with your ceviche",
 "howlong":"Poured fresh at the bar",
 "includes":"Micheladas garnished and rimmed, aguas frescas with one free refill",
 "items":[("Micheladas","Cold beer built up with lime, chile and a salted rim.",""),
          ("Draft Beer","Modelo Especial, Negra Modelo, Pacifico, Estrella, Blue Moon, Tecate, Dos Equis, Big Wave, Bodhizafa.",""),
          ("Margaritas","House margaritas and a rotating tequila selection.",""),
          ("Tequila Thursday","Five dollar tequila pours every Thursday.","$5"),
          ("Aguas Frescas","Horchata, Jamaica, Tamarindo, Pineapple and Melon. Mexican Coke in the bottle.","")]},
]

STAR='<svg viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4"><path d="M12 2l2.9 6.26L22 9.27l-5 4.87L18.18 22 12 18.56 5.82 22 7 14.14l-5-4.87 7.1-1.01z"/></svg>'

def stars(n):
    return '<span class="flex text-gold">'+(STAR*int(n))+'</span>'

ICONS={
 "fish":'<path d="M3 12c3-5 8-7 13-7-1.5 2-1.5 4 0 6-1.5 2-1.5 4 0 6-5 0-10-2-13-5zm13-5c1.5 1 3 2.5 5 5-2 2.5-3.5 4-5 5"/><circle cx="8" cy="11" r="1" fill="currentColor" stroke="none"/>',
 "leaf":'<path d="M11 21c-4 0-7-3-7-7 0-6 6-11 16-11 0 10-5 16-11 16-2 0-3-1-3-3 0-3 4-6 9-7"/>',
 "lime":'<circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18M6 6l12 12M18 6L6 18"/>',
 "bowl":'<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M7 7c0-1 1-2 2-1 1-1 2 0 2 1M13 6c0-1 1-2 2-1"/>',
 "glass":'<path d="M5 4h14l-6 8v6h3v2H8v-2h3v-6z"/>',
 "music":'<path d="M9 18V5l10-2v13"/><circle cx="6" cy="18" r="2.5"/><circle cx="16" cy="16" r="2.5"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin":'<path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "phone":'<path d="M4 4h4l2 5-2.5 1.5a12 12 0 0 0 6 6L15 14l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 2 6a2 2 0 0 1 2-2z"/>',
 "check":'<path d="M20 6L9 17l-5-5"/>',
 "star":'<path d="M12 2l2.9 6.26L22 9.27l-5 4.87L18.18 22 12 18.56 5.82 22 7 14.14l-5-4.87 7.1-1.01z"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5"/><path d="M16 6a3 3 0 0 1 0 6M21 20c0-2-1-3.5-3-4.5"/>',
 "sun":'<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
}
def icon(name,cls="w-7 h-7"):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" class="{cls}">{ICONS[name]}</svg>'

NAV=[("index.html","Inicio"),("menu.html","Menu"),("index.html#especialidades","Especialidades"),
     ("index.html#resenas","Resenas"),("blog.html","Blog")]

def header(active):
    links=""
    for href,label in NAV:
        is_act = (active=="home" and href=="index.html") or (active=="menu" and href=="menu.html") or (active=="blog" and href=="blog.html")
        cls="text-gold" if is_act else "text-cream/85 hover:text-gold"
        links+=f'<a href="{href}" class="{cls} transition font-semibold">{label}</a>'
    mlinks=""
    for href,label in NAV:
        mlinks+=f'<a href="{href}" class="block px-5 py-3 text-cream/90 hover:bg-white/5 hover:text-gold border-b border-white/10 font-semibold">{label}</a>'
    return f'''
<header class="sticky top-0 z-50">
  <div class="bg-navy2 text-cream/80 text-[12.5px]">
    <div class="max-w-6xl mx-auto px-4 py-1.5 flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-center">
      <span class="inline-flex items-center gap-1">{icon("pin","w-3.5 h-3.5 text-gold")} {ADDR}</span>
      <span class="text-gold/50">|</span>
      <span class="inline-flex items-center gap-1">{icon("clock","w-3.5 h-3.5 text-gold")} Closed Tuesdays, open daily till 9</span>
      <span class="text-gold/50">|</span>
      <span class="inline-flex items-center gap-1 text-gold font-semibold">Tequila Thursday $5</span>
    </div>
  </div>
  <div class="bg-navy/95 backdrop-blur border-b border-gold/25">
    <div class="max-w-6xl mx-auto px-4 h-[64px] flex items-center justify-between gap-3">
      <a href="index.html" class="flex items-center gap-2.5 shrink-0">
        <span class="grid place-items-center w-9 h-9 rounded-full bg-gold text-navy shrink-0">{icon("fish","w-5 h-5")}</span>
        <span class="leading-none">
          <span class="block font-display text-gold text-[19px] tracking-wide">EL VIEJON</span>
          <span class="block text-cream/70 text-[10px] tracking-[0.25em] uppercase">Mariscos y Cantina</span>
        </span>
      </a>
      <nav class="hidden md:flex items-center gap-6 text-[14.5px]">{links}</nav>
      <div class="hidden md:flex items-center gap-2 shrink-0">
        <a href="tel:{TEL}" class="inline-flex items-center gap-1.5 bg-gold text-navy font-bold px-4 py-2 rounded-full hover:brightness-95 transition text-[14px]">{icon("phone","w-4 h-4")} Call</a>
      </div>
      <button id="navBtn" aria-label="Menu" class="md:hidden grid place-items-center w-10 h-10 rounded-lg text-cream hover:bg-white/10">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="w-6 h-6"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
    <div id="navMenu" style="display:none" class="md:hidden bg-navy border-t border-gold/20">
      {mlinks}
      <a href="tel:{TEL}" class="block px-5 py-3 bg-gold text-navy font-bold text-center">Call {PHONE}</a>
    </div>
  </div>
</header>'''

def footer():
    hrows=""
    for d,h in HOURS:
        cl="text-chili font-semibold" if h=="Closed" else "text-cream/85"
        hrows+=f'<div class="flex justify-between gap-4 py-1 border-b border-white/10"><span class="text-cream/70">{d}</span><span class="{cl}">{h}</span></div>'
    return f'''
<footer id="contacto" class="bg-navy2 text-cream/80">
  <div class="max-w-6xl mx-auto px-4 py-12 grid gap-10 md:grid-cols-3">
    <div>
      <div class="flex items-center gap-2.5 mb-3">
        <span class="grid place-items-center w-9 h-9 rounded-full bg-gold text-navy">{icon("fish","w-5 h-5")}</span>
        <span class="font-display text-gold text-xl">EL VIEJON</span>
      </div>
      <p class="text-sm leading-relaxed text-cream/70">Fresh seafood, mariscos and Mexican plates with a full cantina, on Caldwell Boulevard in Nampa. Family run and proudly Latino owned.</p>
      <div class="flex items-center gap-1 mt-4">{stars(5)}<span class="text-cream/70 text-sm ml-2">{RATING} from {RCOUNT} Google reviews</span></div>
    </div>
    <div>
      <h3 class="font-display text-gold text-lg mb-3">Visit Us</h3>
      <p class="flex items-start gap-2 text-sm mb-2">{icon("pin","w-4 h-4 text-gold mt-0.5 shrink-0")} <a class="hover:text-gold" href="{MAPS}" target="_blank" rel="noopener">{ADDR}</a></p>
      <p class="flex items-center gap-2 text-sm mb-2">{icon("phone","w-4 h-4 text-gold shrink-0")} <a class="hover:text-gold" href="tel:{TEL}">{PHONE}</a></p>
      <a href="{MAPS}" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 mt-2 bg-gold text-navy font-bold px-4 py-2 rounded-full text-sm hover:brightness-95">{icon("pin","w-4 h-4")} Get Directions</a>
    </div>
    <div>
      <h3 class="font-display text-gold text-lg mb-3">Hours</h3>
      <div class="text-sm">{hrows}</div>
    </div>
  </div>
  <div class="border-t border-white/10">
    <div class="max-w-6xl mx-auto px-4 py-5 text-center text-xs text-cream/55">
      &copy; <span id="yr"></span> {NAME}. Nampa, Idaho. Reviews and ratings shown are real and unaltered from Google.
    </div>
  </div>
</footer>'''

FONTS='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'''

TWCONF='''<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={theme:{extend:{colors:{navy:'#102a47',navy2:'#0a1d33',gold:'#d99e2b',gold2:'#b9831c',cream:'#f7f1e6',chili:'#d4502e',ink:'#1c1a17'},fontFamily:{display:['"Alfa Slab One"','serif'],sans:['Inter','sans-serif']}}}}</script>'''

CSS='''<style>
html{scroll-behavior:smooth}body{font-family:Inter,sans-serif;background:#f7f1e6;color:#1c1a17;overflow-x:hidden}
.font-display{font-family:"Alfa Slab One",serif;font-weight:400}
.marq{display:flex;gap:0;white-space:nowrap;animation:marq 30s linear infinite}
.marq:hover{animation-play-state:paused}
@keyframes marq{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.rev-track{display:flex;gap:1rem;width:max-content;animation:rev 48s linear infinite}
.rev-wrap:hover .rev-track{animation-play-state:paused}
@keyframes rev{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.marq,.rev-track{animation:none}}
.hero-img{filter:saturate(1.05)}
</style>'''

SCRIPTS=f'''<script>
document.getElementById('yr').textContent=new Date().getFullYear();
(function(){{var b=document.getElementById('navBtn'),m=document.getElementById('navMenu');
if(b&&m){{b.addEventListener('click',function(){{m.style.display=(m.style.display==='none'||!m.style.display)?'block':'none';}});}}}})();
</script>'''

def page(title,desc,slug,jsonld,main_html,active):
    canon=f"{SITE}/{slug}"
    jl=""
    for j in jsonld:
        jl+='<script type="application/ld+json">'+json.dumps(j)+'</script>\n'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="restaurant"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/img/torre-mariscos.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' fill='%23102a47'/%3E%3Ctext x='12' y='17' font-size='13' text-anchor='middle' fill='%23d99e2b' font-family='serif'%3EV%3C/text%3E%3C/svg%3E">
{FONTS}
{TWCONF}
{CSS}
{jl}</head>
<body>
{header(active)}
{main_html}
{footer()}
{SCRIPTS}
</body>
</html>'''

def review_card(r,cls=""):
    name,when,rt,txt=r
    return f'''<figure class="bg-white rounded-2xl border border-navy/10 shadow-sm p-5 flex flex-col h-full {cls}">
      <div class="flex items-center gap-1 mb-2">{stars(rt)}</div>
      <blockquote class="text-[14.5px] leading-relaxed text-ink/85 flex-1">{html.escape(txt)}</blockquote>
      <figcaption class="mt-3 pt-3 border-t border-navy/10 flex items-center gap-3">
        <span class="grid place-items-center w-9 h-9 rounded-full bg-navy text-gold font-bold text-sm">{html.escape(name[0])}</span>
        <span><span class="block font-semibold text-navy text-sm">{html.escape(name)}</span><span class="block text-ink/50 text-xs">{when} on Google</span></span>
      </figcaption>
    </figure>'''

# build carousel track (duplicated for seamless loop)
def rev_carousel():
    cards="".join(f'<div class="w-[320px] shrink-0">{review_card(r)}</div>' for r in REVIEWS)
    return f'''<div class="rev-wrap overflow-hidden py-2"><div class="rev-track">{cards}{cards}</div></div>'''

print("loaded")

# ---------- HERO + sections for index ----------
SPECIALS=["Aguachile Verde","Ceviche de Camaron","Torre de Mariscos","Coctel de Camaron","Quesabirria",
"Caldo de Mariscos","Tacos de Asada","Micheladas","Botana El Viejon","Tostada de Ceviche","Tequila Thursday $5","Live Music Weekends"]

GALLERY=[("torre-mariscos.jpg","Torre de mariscos, the signature seafood tower"),
("aguachile.jpg","Aguachile verde with shrimp and cucumber"),
("coctel-camaron.jpg","Coctel de camaron, a cold shrimp cocktail"),
("ceviche-tostada.jpg","Tostada de ceviche topped with avocado"),
("botana-platter.jpg","Botana El Viejon mixed seafood platter"),
("molcajete.jpg","Seafood molcajete served bubbling hot"),
("caldo-mariscos.jpg","Caldo de mariscos, a hearty seafood soup"),
("birria-tacos.jpg","Quesabirria with consome for dipping"),
("tacos-asada.jpg","Tacos de asada off the grill"),
("michelada.jpg","A michelada built tall at the cantina"),
("interior-comedor.jpg","The dining room at Mariscos El Viejon"),
("cantina-bar.jpg","The full cantina bar and weekend crowd"),
("interior-mesas.jpg","Family friendly seating and decor"),
("plato-marino.jpg","A fresh seafood plate from the kitchen")]

FEATS=[("lime","Cured fresh, served cold","Ceviches and aguachiles made to order, the reason reviewers say the seafood here tastes clean and bright with no fishy smell."),
("users","A full cantina, not just beer","Micheladas, margaritas, a long beer list and five dollar Tequila Thursdays, with live music and families on the weekends."),
("star","Worth the drive in Nampa","A 4.5 from more than 660 Google reviews, with regulars who name their server and come back to work through the whole menu.")]

STEPS=[("pin","Come in or call ahead","Find us at 1125 Caldwell Blvd in Nampa. Dine in for the full cantina experience, or call for takeout."),
("lime","Start with a ceviche","Open with an aguachile, a ceviche or a cold coctel. Add a michelada while you look over the menu."),
("glass","Share the tower","Order the Torre de Mariscos for the table, try a caldo or quesabirria, and stay for the weekend live music.")]

FAQ=[("Where is Mariscos El Viejon located?","We are at 1125 Caldwell Blvd, Nampa, ID 83651, near the corner of Caldwell Boulevard and Karcher, with parking and outdoor seating."),
("What are your hours?","We are open Monday, Wednesday, Thursday and Sunday from 11 AM to 9 PM, Friday and Saturday from 11 AM to 9:30 PM, and we are closed on Tuesdays."),
("Do you have a full bar?","Yes. We are a full cantina with micheladas, margaritas, draft and imported beer, and five dollar tequila every Thursday."),
("What is the most popular dish?","The Torre de Mariscos, our seafood tower, is the dish guests photograph and share most. Our ceviches, aguachiles and quesabirria are close behind."),
("Is there food for people who do not eat seafood?","Absolutely. We serve burritos, quesadillas, chimichangas, tacos de asada, fajitas and a kids menu alongside our mariscos."),
("Do you have live music?","Yes, on weekends you will often find live music and a lively, family friendly crowd.")]

def build_index():
    # marquee
    chips="".join(f'<span class="inline-flex items-center gap-2 px-5 text-cream/90"><span class="w-1.5 h-1.5 rounded-full bg-gold"></span>{html.escape(s)}</span>' for s in SPECIALS)
    marquee=f'<div class="bg-navy py-3 overflow-hidden border-y border-gold/20"><div class="marq font-semibold text-[15px]">{chips}{chips}</div></div>'
    feats="".join(f'''<div class="bg-white rounded-2xl border border-navy/10 p-6 shadow-sm">
      <div class="grid place-items-center w-12 h-12 rounded-xl bg-gold/15 text-gold2 mb-4">{icon(ic)}</div>
      <h3 class="font-display text-navy text-lg mb-2">{html.escape(t)}</h3><p class="text-ink/70 text-[14.5px] leading-relaxed">{html.escape(d)}</p></div>''' for ic,t,d in FEATS)
    # service cards
    cards=""
    for c in CATS:
        cards+=f'''<a href="{c['slug']}.html" class="group bg-white rounded-2xl border border-navy/10 shadow-sm overflow-hidden flex flex-col h-full hover:shadow-lg hover:-translate-y-0.5 transition">
        <div class="aspect-[4/3] overflow-hidden"><img src="img/{c['img']}" alt="{html.escape(c['alt'])}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition duration-500"></div>
        <div class="p-5 flex flex-col flex-1">
          <span class="text-gold2 text-[11px] font-bold uppercase tracking-wide">{html.escape(c['tag'])}</span>
          <h3 class="font-display text-navy text-[19px] mt-1 mb-2 leading-tight">{html.escape(c['name'])}</h3>
          <p class="text-ink/70 text-[14px] leading-relaxed flex-1">{html.escape(c['blurb'][:120])}...</p>
          <span class="mt-4 inline-flex items-center gap-1 text-navy font-bold text-sm group-hover:text-gold2">See the menu {icon("check","w-4 h-4 hidden")}<svg viewBox="0 0 24 24" class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
        </div></a>'''
    steps="".join(f'''<div class="relative bg-navy text-cream rounded-2xl p-6">
      <div class="grid place-items-center w-12 h-12 rounded-xl bg-gold text-navy mb-4">{icon(ic)}</div>
      <span class="absolute top-5 right-6 font-display text-gold/30 text-3xl">{i+1}</span>
      <h3 class="font-display text-gold text-lg mb-2">{html.escape(t)}</h3><p class="text-cream/75 text-[14.5px] leading-relaxed">{html.escape(d)}</p></div>''' for i,(ic,t,d) in enumerate(STEPS))
    gal="".join(f'<figure class="overflow-hidden rounded-xl group"><img src="img/{f}" alt="{html.escape(a)}" loading="lazy" class="w-full h-56 object-cover group-hover:scale-105 transition duration-500"></figure>' for f,a in GALLERY)
    grid6="".join(f'<div>{review_card(r)}</div>' for r in REVIEWS[:6])
    faqs="".join(f'''<details class="group bg-white rounded-xl border border-navy/10 p-4">
      <summary class="flex justify-between items-center cursor-pointer font-semibold text-navy text-[15px] list-none">{html.escape(q)}<span class="text-gold2 group-open:rotate-45 transition text-xl leading-none">+</span></summary>
      <p class="mt-3 text-ink/70 text-[14.5px] leading-relaxed">{html.escape(a)}</p></details>''' for q,a in FAQ)

    main=f'''
<section class="relative bg-navy text-cream overflow-hidden">
  <div class="absolute inset-0"><img src="img/botana-platter.jpg" alt="" class="hero-img w-full h-full object-cover opacity-25"></div>
  <div class="absolute inset-0 bg-gradient-to-r from-navy via-navy/90 to-navy/40"></div>
  <div class="relative max-w-6xl mx-auto px-4 py-20 md:py-28 grid md:grid-cols-2 gap-10 items-center">
    <div>
      <span class="inline-flex items-center gap-2 bg-gold/15 text-gold border border-gold/30 rounded-full px-3 py-1 text-xs font-bold uppercase tracking-wide">Latino owned, Nampa Idaho</span>
      <h1 class="font-display text-4xl md:text-6xl leading-[1.05] mt-4">Fresh mariscos,<br><span class="text-gold">cold ceviche,</span><br>a full cantina.</h1>
      <p class="mt-5 text-cream/80 text-lg max-w-md leading-relaxed">Seafood towers, aguachiles, quesabirria and micheladas on Caldwell Boulevard. The Nampa mariscos spot folks drive across the valley for.</p>
      <div class="mt-7 flex flex-wrap gap-3">
        <a href="tel:{TEL}" class="inline-flex items-center gap-2 bg-gold text-navy font-bold px-6 py-3 rounded-full hover:brightness-95 transition">{icon("phone","w-5 h-5")} Call to Order</a>
        <a href="menu.html" class="inline-flex items-center gap-2 bg-white/10 border border-white/25 text-cream font-bold px-6 py-3 rounded-full hover:bg-white/20 transition">See the Menu</a>
      </div>
      <div class="mt-8 flex flex-wrap gap-3">
        <div class="bg-white/10 backdrop-blur border border-white/15 rounded-xl px-4 py-3">
          <div class="flex items-center gap-1">{stars(5)}<span class="font-bold ml-1">{RATING}</span></div>
          <div class="text-cream/70 text-xs mt-0.5">{RCOUNT} Google reviews</div></div>
        <div class="bg-white/10 backdrop-blur border border-white/15 rounded-xl px-4 py-3">
          <div class="font-bold flex items-center gap-1.5">{icon("glass","w-4 h-4 text-gold")} Full Cantina</div>
          <div class="text-cream/70 text-xs mt-0.5">Micheladas and margaritas</div></div>
        <div class="bg-white/10 backdrop-blur border border-white/15 rounded-xl px-4 py-3">
          <div class="font-bold flex items-center gap-1.5">{icon("music","w-4 h-4 text-gold")} Live Music</div>
          <div class="text-cream/70 text-xs mt-0.5">Weekends, family friendly</div></div>
      </div>
    </div>
    <div class="hidden md:block">
      <div class="relative">
        <img src="img/torre-mariscos.jpg" alt="Torre de mariscos seafood tower" class="rounded-3xl shadow-2xl w-full object-cover aspect-[4/5] border-4 border-white/10">
        <div class="absolute -bottom-5 -left-5 bg-white text-navy rounded-2xl shadow-xl px-5 py-3">
          <div class="font-display text-2xl text-gold2">Torre de Mariscos</div>
          <div class="text-ink/60 text-xs">our signature seafood tower</div></div>
      </div>
    </div>
  </div>
</section>
{marquee}

<section class="max-w-6xl mx-auto px-4 py-16">
  <div class="text-center max-w-2xl mx-auto mb-10">
    <h2 class="font-display text-navy text-3xl md:text-4xl">Why folks keep coming back</h2>
    <p class="text-ink/65 mt-3">A real mariscos kitchen, a lively cantina, and a welcome that feels like family.</p>
  </div>
  <div class="grid md:grid-cols-3 gap-5">{feats}</div>
</section>

<section id="especialidades" class="bg-cream">
  <div class="max-w-6xl mx-auto px-4 py-16">
    <div class="flex flex-wrap items-end justify-between gap-4 mb-8">
      <div><h2 class="font-display text-navy text-3xl md:text-4xl">Our specialties</h2>
      <p class="text-ink/65 mt-2">From cold ceviche to the seafood tower, tacos to the cantina. Tap any one for the full menu.</p></div>
      <a href="menu.html" class="inline-flex items-center gap-1.5 text-navy font-bold hover:text-gold2">Full menu <svg viewBox="0 0 24 24" class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{cards}</div>
  </div>
</section>

<section class="max-w-6xl mx-auto px-4 py-16">
  <div class="text-center max-w-2xl mx-auto mb-10"><h2 class="font-display text-navy text-3xl md:text-4xl">How to do El Viejon</h2>
  <p class="text-ink/65 mt-3">Three easy steps to the best seat in the house.</p></div>
  <div class="grid md:grid-cols-3 gap-5">{steps}</div>
</section>

<section class="bg-navy2">
  <div class="max-w-6xl mx-auto px-4 py-16">
    <div class="text-center max-w-2xl mx-auto mb-10"><h2 class="font-display text-gold text-3xl md:text-4xl">From our tables</h2>
    <p class="text-cream/70 mt-3">Real photos from Mariscos El Viejon in Nampa.</p></div>
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">{gal}</div>
  </div>
</section>

<section id="resenas" class="max-w-6xl mx-auto px-4 py-16">
  <div class="text-center max-w-2xl mx-auto mb-10">
    <div class="flex justify-center items-center gap-2 mb-2">{stars(5)}<span class="font-bold text-navy text-lg">{RATING}</span><span class="text-ink/55">/ {RCOUNT} reviews</span></div>
    <h2 class="font-display text-navy text-3xl md:text-4xl">What guests are saying</h2>
    <p class="text-ink/65 mt-3">Unedited reviews from real guests on Google.</p>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-8">{grid6}</div>
</section>
{rev_carousel()}

<section class="max-w-6xl mx-auto px-4 py-16 grid md:grid-cols-2 gap-10 items-center">
  <div class="order-2 md:order-1">
    <span class="text-gold2 font-bold uppercase text-xs tracking-wide">Our story</span>
    <h2 class="font-display text-navy text-3xl md:text-4xl mt-2 mb-4">A family mariscos kitchen and cantina</h2>
    <p class="text-ink/75 leading-relaxed mb-3">Mariscos El Viejon is a Latino owned seafood and Mexican restaurant on Caldwell Boulevard in Nampa. We built our name on fresh ceviche, generous seafood towers, and a warm, lively room where the bar pours micheladas and the weekends fill with live music and families.</p>
    <p class="text-ink/75 leading-relaxed mb-5">Guests tell us the seafood tastes clean and bright, the portions are generous, and the service makes first timers feel like regulars. Come hungry, bring the family, and let us walk you through the menu.</p>
    <div class="flex flex-wrap gap-3">
      <a href="tel:{TEL}" class="inline-flex items-center gap-2 bg-navy text-cream font-bold px-5 py-2.5 rounded-full hover:bg-navy2 transition">{icon("phone","w-4 h-4")} {PHONE}</a>
      <a href="{MAPS}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 border border-navy/25 text-navy font-bold px-5 py-2.5 rounded-full hover:bg-navy hover:text-cream transition">Get Directions</a>
    </div>
  </div>
  <div class="order-1 md:order-2"><img src="img/cantina-bar.jpg" alt="The cantina bar at Mariscos El Viejon" class="rounded-3xl shadow-xl w-full object-cover aspect-[5/4]"></div>
</section>

<section class="bg-cream border-y border-navy/10">
  <div class="max-w-6xl mx-auto px-4 py-14 grid md:grid-cols-2 gap-8 items-center">
    <div>
      <span class="text-gold2 font-bold uppercase text-xs tracking-wide">From the blog</span>
      <h2 class="font-display text-navy text-2xl md:text-3xl mt-2 mb-3">A first timer's guide to ordering mariscos in Nampa</h2>
      <p class="text-ink/70 leading-relaxed mb-4">New to ceviche, aguachile and the seafood tower? Here is exactly what to order on your first visit, plus a two host podcast you can listen to on the way over.</p>
      <a href="blog.html" class="inline-flex items-center gap-1.5 bg-navy text-cream font-bold px-5 py-2.5 rounded-full hover:bg-navy2 transition">Read the guide <svg viewBox="0 0 24 24" class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
    <img src="img/ceviche-tostada.jpg" alt="Tostada de ceviche" class="rounded-2xl shadow-lg w-full object-cover aspect-[16/10]">
  </div>
</section>

<section class="max-w-3xl mx-auto px-4 py-16">
  <h2 class="font-display text-navy text-3xl text-center mb-8">Questions, answered</h2>
  <div class="space-y-3">{faqs}</div>
</section>

<section class="bg-navy text-cream">
  <div class="max-w-4xl mx-auto px-4 py-16 text-center">
    <h2 class="font-display text-3xl md:text-4xl">Hungry yet?</h2>
    <p class="text-cream/80 mt-3 max-w-xl mx-auto">Call ahead for takeout or come in and grab a table. Closed Tuesdays, open the rest of the week.</p>
    <div class="mt-7 flex flex-wrap gap-3 justify-center">
      <a href="tel:{TEL}" class="inline-flex items-center gap-2 bg-gold text-navy font-bold px-6 py-3 rounded-full hover:brightness-95 transition">{icon("phone","w-5 h-5")} {PHONE}</a>
      <a href="{MAPS}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-white/10 border border-white/25 font-bold px-6 py-3 rounded-full hover:bg-white/20 transition">{icon("pin","w-5 h-5")} Directions</a>
    </div>
  </div>
</section>'''
    jsonld=[
     {"@context":"https://schema.org","@type":"Restaurant","name":NAME,"servesCuisine":["Mexican","Seafood","Mariscos"],
      "image":f"{SITE}/img/torre-mariscos.jpg","@id":SITE,"url":SITE,"telephone":"+1-208-910-9471","priceRange":"$$",
      "address":{"@type":"PostalAddress","streetAddress":"1125 Caldwell Blvd","addressLocality":"Nampa","addressRegion":"ID","postalCode":"83651","addressCountry":"US"},
      "geo":{"@type":"GeoCoordinates","latitude":43.5999975,"longitude":-116.5956566},
      "hasMenu":f"{SITE}/menu.html",
      "openingHoursSpecification":[
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Wednesday","Thursday","Sunday"],"opens":"11:00","closes":"21:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Friday","Saturday"],"opens":"11:00","closes":"21:30"}],
      "aggregateRating":{"@type":"AggregateRating","ratingValue":RATING,"reviewCount":RCOUNT}},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
    ]
    return page(f"{NAME} | Seafood, Mariscos and Cantina in Nampa, ID",
      "Fresh ceviche, aguachiles, seafood towers, quesabirria and micheladas. A 4.5 star Latino owned mariscos restaurant and full cantina on Caldwell Blvd in Nampa, Idaho.",
      "index.html",jsonld,main,"home")
print("part2 loaded")

def crumb(active_name):
    return f'''<nav class="bg-cream border-b border-navy/10"><div class="max-w-5xl mx-auto px-4 py-3 text-sm text-ink/60"><a href="index.html" class="hover:text-gold2">Inicio</a> <span class="text-ink/30">/</span> <a href="menu.html" class="hover:text-gold2">Menu</a> <span class="text-ink/30">/</span> <span class="text-navy font-semibold">{html.escape(active_name)}</span></div></nav>'''

def build_menu():
    cards=""
    for c in CATS:
        cards+=f'''<a href="{c['slug']}.html" class="group bg-white rounded-2xl border border-navy/10 shadow-sm overflow-hidden flex flex-col h-full hover:shadow-lg hover:-translate-y-0.5 transition">
        <div class="aspect-[16/10] overflow-hidden"><img src="img/{c['img']}" alt="{html.escape(c['alt'])}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition duration-500"></div>
        <div class="p-5 flex flex-col flex-1">
          <span class="text-gold2 text-[11px] font-bold uppercase tracking-wide">{html.escape(c['tag'])}</span>
          <h3 class="font-display text-navy text-xl mt-1 mb-2 leading-tight">{html.escape(c['name'])}</h3>
          <p class="text-ink/70 text-[14px] leading-relaxed flex-1">{html.escape(c['blurb'])}</p>
          <span class="mt-4 inline-flex items-center gap-1 text-navy font-bold text-sm group-hover:text-gold2">View {html.escape(c['name'])} <svg viewBox="0 0 24 24" class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
        </div></a>'''
    main=f'''
{crumb("Menu")}
<section class="bg-navy text-cream"><div class="max-w-5xl mx-auto px-4 py-14 text-center">
  <h1 class="font-display text-4xl md:text-5xl">The Menu</h1>
  <p class="text-cream/80 mt-3 max-w-xl mx-auto">Mariscos, tacos, Mexican plates and a full cantina. Explore each part of the menu below, then call ahead at <a href="tel:{TEL}" class="text-gold font-bold">{PHONE}</a>.</p>
</div></section>
<section class="max-w-6xl mx-auto px-4 py-14">
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{cards}</div>
</section>
<section class="bg-cream border-y border-navy/10"><div class="max-w-6xl mx-auto px-4 py-14">
  <h2 class="font-display text-navy text-2xl text-center mb-8">Guests love it</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{"".join(review_card(r) for r in REVIEWS[:3])}</div>
</div></section>'''
    jsonld=[{"@context":"https://schema.org","@type":"Menu","name":f"{NAME} Menu","url":f"{SITE}/menu.html",
      "hasMenuSection":[{"@type":"MenuSection","name":c["name"],"url":f"{SITE}/{c['slug']}.html"} for c in CATS]}]
    return page(f"Menu | {NAME} Nampa, ID","Explore the full menu at Mariscos El Viejon in Nampa: ceviches, aguachiles, seafood towers, cocteles, quesabirria, tacos, caldos, Mexican plates and a full cantina.","menu.html",jsonld,main,"menu")

def build_category(c, idx):
    items=""
    for nm,desc,price in c["items"]:
        pr=f'<span class="text-gold2 font-bold whitespace-nowrap ml-3">{html.escape(price)}</span>' if price else ''
        items+=f'''<li class="flex justify-between items-start gap-3 py-3 border-b border-navy/10 last:border-0">
          <div><span class="font-semibold text-navy">{html.escape(nm)}</span><p class="text-ink/65 text-[14px] leading-snug mt-0.5">{html.escape(desc)}</p></div>{pr}</li>'''
    # two reviews (rotate)
    r1=REVIEWS[idx % len(REVIEWS)]; r2=REVIEWS[(idx+3) % len(REVIEWS)]
    revs=f'<div class="grid sm:grid-cols-2 gap-5">{review_card(r1)}{review_card(r2)}</div>'
    detail=f'''<div class="grid sm:grid-cols-3 gap-4 my-8">
      <div class="bg-cream rounded-xl p-4 border border-navy/10"><div class="text-gold2 mb-1">{icon("star","w-5 h-5")}</div><div class="font-bold text-navy text-sm">Good for</div><p class="text-ink/70 text-[13.5px] mt-1">{html.escape(c['good_for'])}</p></div>
      <div class="bg-cream rounded-xl p-4 border border-navy/10"><div class="text-gold2 mb-1">{icon("clock","w-5 h-5")}</div><div class="font-bold text-navy text-sm">How it comes</div><p class="text-ink/70 text-[13.5px] mt-1">{html.escape(c['howlong'])}</p></div>
      <div class="bg-cream rounded-xl p-4 border border-navy/10"><div class="text-gold2 mb-1">{icon("check","w-5 h-5")}</div><div class="font-bold text-navy text-sm">Served with</div><p class="text-ink/70 text-[13.5px] mt-1">{html.escape(c['includes'])}</p></div>
    </div>'''
    main=f'''
{crumb(c['name'])}
<section class="bg-navy text-cream overflow-hidden">
  <div class="max-w-5xl mx-auto px-4 py-12 grid md:grid-cols-2 gap-8 items-center">
    <div>
      <span class="text-gold font-bold uppercase text-xs tracking-wide">{html.escape(c['tag'])}</span>
      <h1 class="font-display text-3xl md:text-5xl mt-2 leading-[1.05]">{html.escape(c['name'])}</h1>
      <p class="text-cream/80 mt-4 leading-relaxed">{html.escape(c['blurb'])}</p>
      <div class="mt-6 flex flex-wrap gap-3">
        <a href="tel:{TEL}" class="inline-flex items-center gap-2 bg-gold text-navy font-bold px-5 py-2.5 rounded-full hover:brightness-95 transition">{icon("phone","w-4 h-4")} Call to Order</a>
        <a href="menu.html" class="inline-flex items-center gap-2 bg-white/10 border border-white/25 font-bold px-5 py-2.5 rounded-full hover:bg-white/20 transition">Back to Menu</a>
      </div>
    </div>
    <img src="img/{c['img']}" alt="{html.escape(c['alt'])}" class="rounded-2xl shadow-2xl w-full object-cover aspect-[5/4] border-4 border-white/10">
  </div>
</section>
<section class="max-w-5xl mx-auto px-4 py-12">
  {detail}
  <div class="bg-white rounded-2xl border border-navy/10 shadow-sm p-6 md:p-8">
    <h2 class="font-display text-navy text-2xl mb-2">On the menu</h2>
    <ul>{items}</ul>
    <p class="text-ink/50 text-xs mt-4">Prices where shown are from the in store menu and may change. Seafood items are served fresh, ask your server for today's offerings.</p>
  </div>
</section>
<section class="bg-cream border-y border-navy/10"><div class="max-w-5xl mx-auto px-4 py-12">
  <h2 class="font-display text-navy text-2xl text-center mb-8">What guests say</h2>{revs}
</div></section>
<section class="bg-navy text-cream"><div class="max-w-4xl mx-auto px-4 py-14 text-center">
  <h2 class="font-display text-2xl md:text-3xl">Ready to dig in?</h2>
  <p class="text-cream/80 mt-3">Call ahead for takeout or come in for the full cantina experience.</p>
  <div class="mt-6 flex flex-wrap gap-3 justify-center">
    <a href="tel:{TEL}" class="inline-flex items-center gap-2 bg-gold text-navy font-bold px-6 py-3 rounded-full hover:brightness-95 transition">{icon("phone","w-5 h-5")} {PHONE}</a>
    <a href="{MAPS}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-white/10 border border-white/25 font-bold px-6 py-3 rounded-full hover:bg-white/20 transition">{icon("pin","w-5 h-5")} Directions</a>
  </div>
</div></section>'''
    jsonld=[{"@context":"https://schema.org","@type":"MenuSection","name":c["name"],"url":f"{SITE}/{c['slug']}.html",
      "description":c["blurb"],
      "hasMenuItem":[{"@type":"MenuItem","name":nm,"description":desc} for nm,desc,price in c["items"]]}]
    return page(f"{c['name']} | {NAME} Nampa, ID", c["blurb"][:155], f"{c['slug']}.html", jsonld, main, "menu")

print("part3 loaded")

def build_blog():
    audio=f'''<div class="bg-navy text-cream rounded-2xl p-5 my-8 not-prose">
      <div class="flex items-center gap-3 mb-3">
        <span class="grid place-items-center w-11 h-11 rounded-full bg-gold text-navy">{icon("music","w-5 h-5")}</span>
        <div><div class="font-display text-gold text-lg leading-none">Listen: Treasure Valley Eats</div>
        <div class="text-cream/70 text-xs mt-1">A two host guide to Mariscos El Viejon, about 2 minutes</div></div>
      </div>
      <audio controls preload="none" class="w-full"><source src="podcast.mp3" type="audio/mpeg">Your browser does not support audio.</audio>
    </div>'''
    body=f'''
    <p>If you have driven Caldwell Boulevard in Nampa, you have passed it. A steady stream of regulars, a parking lot that fills up on weekends, and a sign that reads <strong>Mariscos El Viejon</strong>. With a 4.5 rating from more than {RCOUNT} Google reviews, this Latino owned seafood and Mexican restaurant has quietly become one of the Treasure Valley's favorite mariscos spots. If it is your first visit, here is exactly how to order.</p>

    <h2>Start cold and bright</h2>
    <p>Mariscos means seafood, and the best way to begin is with something cured and cold. The <strong>aguachile</strong> is raw shrimp swimming in a bright green sauce of lime and serrano chile, layered with cucumber and red onion. It is sharp, citrusy, and just spicy enough to wake up your palate. If you want something a little gentler, the <strong>ceviche de camaron</strong> chops the shrimp into a refreshing mix of lime, tomato, onion, cilantro and avocado, served with crisp tostadas.</p>
    <p>This is the part of the menu reviewers rave about. As one guest put it, most seafood places carry that unpleasant smell, but not here. The seafood tastes clean and fresh, which is the single most important thing a mariscos kitchen can get right.</p>

    {audio}

    <h2>Order the tower for the table</h2>
    <p>If you are with a group, the move is the <strong>Torre de Mariscos</strong>, the seafood tower. It is layers of shrimp, octopus, fish and avocado stacked in a tall glass, equal parts centerpiece and meal. One couple wrote that they split the tower and it was plenty for two. It photographs beautifully, but more importantly, it lets everyone at the table taste a little of everything.</p>
    <p>Not in a sharing mood? The <strong>coctel de camaron</strong> is a cold shrimp cocktail in a tangy tomato and clamato base, loaded with avocado and cilantro. The <strong>campechana</strong> mixes shrimp, octopus and more for the seafood lover who wants it all in one cup.</p>

    <h2>Something warm: the caldos</h2>
    <p>Idaho evenings can turn cool fast, and that is when the <strong>caldos</strong> shine. The caldo de mariscos, a seven seas style soup, comes loaded with shrimp and fresh fish in a deep, savory broth. Regulars order it when they want something hearty and comforting, and it pairs perfectly with warm tortillas and a squeeze of lime.</p>

    <h2>Not into seafood? You are still covered</h2>
    <p>One of the smartest things about El Viejon is that it is not seafood only. Bring a friend who does not eat fish and they will eat well. The <strong>quesabirria</strong> arrives with a cup of rich consome for dipping, the tacos de asada come straight off the grill, and there is a full lineup of burritos, quesadillas, chimichangas and fajitas. Burritos start around nine dollars, and there is a kids menu that keeps the little ones happy. As one reviewer noted, the menu is filled with many options.</p>

    <h2>This is a full cantina</h2>
    <p>Do not sleep on the bar. El Viejon is a full cantina, not just a beer fridge. <strong>Micheladas</strong> come built tall with lime, chile and a salted rim, the margaritas flow, and the draft and import list runs long: Modelo, Negra Modelo, Pacifico, Dos Equis and more. Come on a Thursday and tequila pours are five dollars. As a few guests pointed out with delight, they have a bar, not just beers.</p>

    <h2>Come on a weekend for the full experience</h2>
    <p>Weekends are when the room really comes alive. Live music, families, kids, and what one reviewer described as all types of people enjoying the time out. There is outdoor seating when the weather is nice, and a service team that gets named in reviews. A server named Richard keeps coming up for walking first timers through the menu, which is the surest sign of a real neighborhood spot.</p>

    <h2>First timer's game plan</h2>
    <p>Here is the short version. Go hungry. Start with an aguachile or a ceviche and a cold michelada. If you are with a group, order the Torre de Mariscos. Add a caldo if it is chilly, or a quesabirria for the table. Save room, because the portions are generous. And if you are not sure what to get, just ask. That is exactly what the regulars did before they became regulars.</p>
    <p>Mariscos El Viejon is at {ADDR}, open Monday, Wednesday, Thursday and Sunday from 11 AM to 9 PM, Friday and Saturday until 9:30 PM, and closed Tuesdays. Call <a href="tel:{TEL}">{PHONE}</a> to order ahead, or just come in and grab a table. Buen provecho.</p>
    '''
    main=f'''
{crumb("Blog")}
<article class="max-w-3xl mx-auto px-4 py-12">
  <div class="text-center mb-8">
    <span class="text-gold2 font-bold uppercase text-xs tracking-wide">First timer's guide</span>
    <h1 class="font-display text-navy text-3xl md:text-4xl mt-2 leading-tight">What to Order at Mariscos El Viejon, Nampa's Seafood and Cantina Favorite</h1>
    <p class="text-ink/55 mt-3 text-sm">A guide from the team at Mariscos El Viejon</p>
  </div>
  <img src="img/aguachile.jpg" alt="Aguachile at Mariscos El Viejon" class="rounded-2xl shadow-lg w-full object-cover aspect-[16/9] mb-8">
  <div class="prose-custom text-ink/85 leading-relaxed space-y-4 [&_h2]:font-display [&_h2]:text-navy [&_h2]:text-2xl [&_h2]:mt-8 [&_h2]:mb-2 [&_a]:text-gold2 [&_a]:font-semibold [&_strong]:text-navy">
  {body}
  </div>
</article>
<section class="bg-cream border-t border-navy/10"><div class="max-w-5xl mx-auto px-4 py-12">
  <h2 class="font-display text-navy text-2xl text-center mb-8">More from our guests</h2>
  <div class="grid sm:grid-cols-3 gap-5">{"".join(review_card(r) for r in REVIEWS[4:7])}</div>
  <div class="text-center mt-8"><a href="menu.html" class="inline-flex items-center gap-2 bg-navy text-cream font-bold px-6 py-3 rounded-full hover:bg-navy2 transition">See the full menu</a></div>
</div></section>'''
    jsonld=[{"@context":"https://schema.org","@type":"BlogPosting",
      "headline":"What to Order at Mariscos El Viejon, Nampa's Seafood and Cantina Favorite",
      "image":f"{SITE}/img/aguachile.jpg","author":{"@type":"Organization","name":NAME},
      "publisher":{"@type":"Organization","name":NAME},"datePublished":"2026-06-22","mainEntityOfPage":f"{SITE}/blog.html",
      "description":"A first timer's guide to ordering at Mariscos El Viejon in Nampa: ceviche, aguachile, the seafood tower, caldos, quesabirria and the cantina."}]
    return page(f"What to Order at {NAME} | Nampa Seafood Guide",
      "A first timer's guide to Mariscos El Viejon in Nampa: ceviche, aguachile, the Torre de Mariscos seafood tower, caldos, quesabirria and the full cantina. With a two host podcast.",
      "blog.html",jsonld,main,"blog")

def write(fn,content):
    with open(os.path.join(OUT,fn),"w",encoding="utf-8") as f: f.write(content)

write("index.html",build_index())
write("menu.html",build_menu())
for i,c in enumerate(CATS):
    write(f"{c['slug']}.html",build_category(c,i))
write("blog.html",build_blog())
# robots, sitemap, nojekyll
urls=["index.html","menu.html","blog.html"]+[f"{c['slug']}.html" for c in CATS]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    loc=f"{SITE}/" if u=="index.html" else f"{SITE}/{u}"
    sm+=f"  <url><loc>{loc}</loc><lastmod>2026-06-22</lastmod></url>\n"
sm+="</urlset>\n"
write("sitemap.xml",sm)
write("robots.txt",f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
write(".nojekyll","")
print("WROTE", len(urls), "pages")
