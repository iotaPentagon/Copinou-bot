import os
import discord
import random
from dotenv import load_dotenv

load_dotenv(dotenv_path = ".env")

client = discord.Client()	


lst = [("émirats arabes unis", "emirats arabes unis", "Abou Dabi"),
("nigéria", "nigeria", "Abuja"),
("ghana", "ghana", "Accra"),
("turkménistan", "turkmenistan", "Achgabat"),
("éthiopie", "ethiopie", "Addis-Abeba"),
("algérie", "algerie", "Alger"),
("niué", "niue", "Alofi"),
("jordanie", "jordanie", "Amman"),
("pays-bas", "pays-bas", "Amsterdam"),
("andorre", "andorre", "Andorre-la-Vieille"),
("turquie", "turquie", "Ankara"),
("madagascar", "madagascar", "Antananarivo"),
("samoa", "samoa", "Apia"),
("erythrée", "erythree", "Asmara"),
("paraguay", "paraguay", "Asuncion"),
("grèce", "grece", "Athènes"),
("îles cook", "iles cook", "Avarua"),
("irak", "irak", "Bagdad"),
("azerbaïdjan", "azerbaidjan", "Bakou"),
("mali", "mali", "Bamako"),
("brunei", "brunei", "Bandar Seri Begawan"),
("thaïlande", "thailande", "Bangkok"),
("république centrafricaine", "republique centrafricaine", "Bangui"),
("gambie", "gambie", "Banjul"),
("saint-christophe-et-niévès", "saint-christophe-et-nieves", "Basseterre"),
("serbie", "serbie", "Belgrade"),
("belize", "belize", "Belmopan"),
("allemagne", "allemagne", "Berlin"),
("suisse", "suisse", "Berne"),
("liban", "liban", "Beyrouth"),
("kirghizistan", "kirghizistan", "Bichkek"),
("guinée-bissau", "guinee-bissau", "Bissau"),
("afrique du sud", "afrique du sud", "Bloemfontein (capitale judiciaire) / Le Cap (capitale législative) / Pretoria (capitale administrative)"),
("colombie", "colombie", "Bogota"),
("brésil", "bresil", "Brasilia"),
("slovaquie", "slovaquie", "Bratislava"),
("république du congo", "republique du congo", "Brazzaville"),
("barbade", "barbade", "Bridgetown"),
("belgique", "belgique", "Bruxelles"),
("roumanie", "roumanie", "Bucarest"),
("hongrie", "hongrie", "Budapest"),
("argentine", "argentine", "Buenos Aires"),
("égypte", "egypte", "Le Caire"),
("australie", "australie", "Canberra"),
("venezuela", "venezuela", "Caracas"),
("sainte-lucie", "sainte-lucie", "Castries"),
("moldavie", "moldavie", "Chisinau"),
("sri lanka", "sri lanka", "Sri Jayawardenapura Kotte"),
("guinée", "guinee", "Conakry"),
("danemark", "danemark", "Copenhague"),
("sénégal", "senegal", "Dakar"),
("syrie", "syrie", "Damas"),
("îles marshall", "iles marshall", "Delap-Uliga-Darrit (Majuro)"),
("bangladesh", "bangladesh", "Dacca"),
("timor oriental", "timor oriental", "Dili"),
("djibouti", "djibouti", "Djibouti"),
("soudan du sud", "soudan du sud", "Djoubanote"),
("tanzanie", "tanzanie", "Dodoma"),
("qatar", "qatar", "Doha"),
("tadjikistan", "tadjikistan", "Douchanbé"),
("irlande", "irlande", "Dublin"),
("arménie", "armenie", "Erevan"),
("sierra leone", "sierra leone", "Freetown"),
("tuvalu", "tuvalu", "Funafuti (Vaiaku)"),
("botswana", "bostwana", "Gaborone"),
("guyana", "guyana", "Georgetown"),
("burundi", "burundi", "Gitega"),
("guatemala", "guatemala", "Guatemala"),
("viêtnam", "vietnam", "Hanoï"),
("zimbabwe", "zimbabwe", "Harare"),
("cuba", "cuba", "La Havane"),
("finlande", "finlande", "Helsinki"),
("îles salomon", "iles salomon", "Honiara"),
("pakistan", "pakistan", "Islamabad"),
("indonésie", "indonesie", "Jakarta"),
("israël", "israel", "Jérusalem"),
("palestine", "palestine", "Ramallah"),
("afghanistan", "afghanistan", "Kaboul"),
("ouganda", "ouganda", "Kampala"),
("népal", "nepal", "Katmandou"),
("soudan", "soudan", "Khartoum"),
("ukraine", "ukraine", "Kiev"),
("rwanda", "rwanda", "Kigali"),
("jamaïque", "jamaique", "Kingston"),
("saint-vincent-et-les-grenadines", "saint-vincent-et-les-grenadines", "Kingstown"),
("république démocratique du congo", "republique democratique du congo", "Kinshasa"),
("palaos", "palaos", "Melekeok"),
("koweït", "koweit", "Koweït"),
("malaisie", "malaisie", "Kuala Lumpur / Putrajaya (capitale administrative)"),
("gabon", "gabon", "Libreville"),
("malawi", "malawi", "Lilongwe"),
("pérou", "perou", "Lima"),
("portugal", "portugal", "Lisbonne"),
("slovénie", "slovenie", "Ljubljana"),
("togo", "togo", "Lomé"),
("royaume-uni", "royaume-uni", "Londres"),
("angola","angola", "Luanda"),
("gambie", "gambie", "Lusaka"),
("luxembourg", "luxembourg", "Luxembourg"),
("espagne", "espagne", "Madrid"),
("guinée équatoriale", "guinee equatoriale", "Malabo"),
("maldives", "maldives", "Malé"),
("nicaragua", "nicaragua", "Managua"),
("bahreïn", "bahrein", "Manama"),
("philippines", "philippines", "Manille"),
("mozambique", "mozambique", "Maputo"),
("oman", "oman", "Mascate"),
("lesotho", "lesotho", "Maseru"),
("eswatini", "swaziland", "Mbabane"),
("mexique", "mexique", "Mexico"),
("biélorussie", "bielorussie", "Minsk"),
("somalie", "somalie", "Mogadiscio (Muqdisho)"),
("monaco", "monaco", "Monaco"),
("liberia", "liberia", "Monrovia"),
("uruguay", "uruguay", "Montevideo"),
("comores",	"comores", "Moroni"),
("russie", "russie", "Moscou"),
("kenya", "kenya", "Nairobi"),
("bahamas", "bahamas", "Nassau"),
("birmanie", "myanmar", "Naypyidaw"),
("tchad", "tchad", "N'Djaména"),
("inde" , "inde", "New Delhi"),
("niger", "niger", "Niamey"),
("chypre", "chypre", "Nicosie"),
("mauritanie", "mauritanie", "Nouakchott"),
("kazakhstan", "kazakhstan",	"Noursoultan"),
("tonga", "tonga", "Nuku'alofa"),
("norvège", "norvege", "Oslo"),
("canada", "canada", "Ottawa"),
("burkina faso", "burkina faso", "Ouagadougou"),
("mongolie", "mongolie", "Oulan-Bator"),
("états fédérés de micronésie", "etats federes de micronesie",	"Palikir"),
("panama", "panama", "Panama"),
("suriname", "suriname", "Paramaribo"),
("france", "france", "Paris"),
("bolivie", "bolivie", "La Paz (gouvernement et ambassades) / Sucre (constitutionnelle)"),
("chine", "chine", "Pékin"),
("cambodge", "cambodge", "Phnom Penh"),
("monténégro", "montenegro", "Podgorica"),
("papouasie-nouvelle-guinée", "papouasie-nouvelle-guinee", "Port Moresby"),
("haïti", "haiti", "Port-au-Prince"),
("trinité-et-tobago", "trinite-et-tobago", "Port-d'Espagne"),
("maurice", "maurice", "Port-Louis"),
("bénin", "benin", "Porto-Novo"),
("vanuatu", "vanuatu", "Port-Vila"),
("république tchèque", "republique tcheque", "Prague"),
("cap-vert", "cap-vert", "Praia"),
("corée du nord", "coree du nord", "Pyongyang"),
("équateur", "equateur", "Quito"),
("maroc", "maroc", "Rabat"),
("islande", "islande", "Reykjavik"),
("lettonie", "lettonie", "Riga"),
("arabie saoudite", "arabie saoudite", "Riyad"),
("italie", "italie", "Rome"),
("dominique", "dominique", "Roseau"),
("antigua-et-barbuda", "antigua-et-barbuda", "Saint John's"),
("république dominicaine", "republique dominicaine", "Saint-Domingue"),
("grenade", "grenade", "Saint-Georges"),
("saint-marin", "saint-marin", "Saint-Marin"),
("costa rica", "costa rica", "San José"),
("salvador", "salvador", "San Salvador"),
("yémen", "yemen", 	"Sanaa"),
("chili", "chili", "Santiago"),
("sao tomé-et-principe", "sao tome-et-principe", "São Tomé"),
("bosnie-herzégovine", "bosnie-herzegovine", "Sarajevo"),
("corée du sud", "coree du sud", "Séoul"),
("singapour", "singapour", "Singapour"),
("macédoine du nord", "macedoine du nord", "Skopje"),
("bulgarie", "bulgarie", "Sofia"),
("suède", "suede", "Stockholm"),
("fidji", "fidji", "Suva"),
("ouzbékistan", "ouzbekistan", "Tachkent"),
("estonie", "estonie", "Tallinn"),
("kiribati", "kiribati", "Tarawa-Sud"),
("géorgie", "georgie", "Tbilissi"),
("honduras", "honduras", "Tegucigalpa"),
("iran", "iran", "Téhéran"),
("bhoutan", "bhoutan", "Thimphou"),
("albanie", "albanie", "Tirana"),
("japon", "japon", "Tokyo"),
("libye", "lybie", "Tripoli"),
("tunisie", "tunisie", "Tunis"),
("liechtenstein", "liechtenstein", "Vaduz"),
("malte", "malte", "La Valette"),
("pologne", "pologne", "Varsovie"),
("vatican", "vatican", 	"Cité du Vatican"),
("seychelles", "seychelles", "Victoria"),
("autriche", "autriche", "Vienne"),
("laos", "laos", "Vientiane"),
("lituanie", "lituanie", "Vilnius"),
("états-unis", "etats-unis", "Washington D.C."),
("nouvelle-zélande", "nouvelle-zelande", "Wellington"),
("namibie", "namibie", "Windhoek"),
("côte d'ivoire", "cote d'ivoire", "Yamoussoukro"),
("cameroun", "cameroun", "Yaoundé"),
("nauru", "nauru", 	"Yaren"),
("croatie", "croatie", "Zagreb"),
("copinou", "copinou", "Copinouyork")]

@client.event
async def on_ready():
	print("ready")

@client.event
async def on_message(message):
	if message.content.lower() == "!information":
		await message.channel.send("De quel pays voulez-vous connaître la capitale ?")
		def check(m):
			return m.author ==  message.author
		msg = await client.wait_for("message", check=check)
		try:
			est_dans_la_liste = False
			for triplet in lst:
				if (triplet[0] in msg.content.lower()) or (triplet[1] in msg.content.lower()):
					await msg.channel.send("La capitale de ce pays est "+ triplet[2])
					est_dans_la_liste = True
					break
			if est_dans_la_liste == False :
				int("")			
		except ValueError :
			await msg.channel.send("Ce pays ne figure pas dans ma liste, êtes-vous sûr de correctement l'orthographier ?")
					
	if ":copinou:" in message.content.lower():
		await message.channel.send("<:copinou_calin:841282748399616041>")

	if message.content.lower() == "!copinou":
		random_triplet = lst[random.randint(0,196)]
		await message.channel.send("/tts message: Quelle est la capitale de ce pays : " + random_triplet[0])
		def check(m):
			return m.author ==  message.author
		msg = await client.wait_for("message", check=check)
		
		if msg.content.lower() != random_triplet[2].lower():
			await msg.channel.send("Raté, c'était " + random_triplet[2])
		else:
			reponse = ["Bien joué !", "Bravo !", "Bonne réponse !", "Félicitations !"]
			await msg.channel.send(reponse[random.randint(0,3)])
		
client.run(os.getenv("TOKEN"))

		
