cities = {
    "głogów": {
        "country": "polska",
        "population": 80000,
        "fact": "W 1109 roku Głogów zasłynął bohaterską, zwycięską obroną grodu przed wojskami niemieckiego króla Henryka V, podczas której mieszkańcy poświęcili życie swoich zakładników, by nie poddać miasta Bolesławowi Krzywoustemu.",
    },
    "ascheberg": {
        "country": "niemcy",
        "population": 16000,
        "fact": "W 1975 roku, w ramach reformy administracyjnej, do gminy Ascheberg włączono dotychczasowe samodzielne miejscowości Herbern oraz Davensberg.",
    },
    "lizbona": {
        "country": "portugalia",
        "population": 550000,
        "fact": "Lizbona jest jedną z najstarszych stolic w Europie, której historia sięga 1200 r. p.n.e., kiedy to została założona przez Fenicjan pod nazwą Olissipo.",
    },
}

for city, city_info in cities.items():
    print(f"\nMiasto {city.title()} to bardzo piękne miasto.")
    print(f"Kraj w którym leży to miasto to {city_info['country'].title()}.")
    print(f"Aktualnie zamieszkuje w nim około {city_info['population']} osób!")
    print(f"Jedną z ciekawostek o tym mieście jest to, że: \n\t{city_info['fact']}")
