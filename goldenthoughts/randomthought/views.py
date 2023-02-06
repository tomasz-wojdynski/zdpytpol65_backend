from django.shortcuts import render, HttpResponse
import random

# Create your views here.


def thought(request):
    THOUGHT_LIST = [
        "Nasze życie jest takim, jakim uczyniły je nasze myśli.  Nie chlubą jest uciec przed śmiercią, lecz uśmiechać "
        "się, gdy i ona się do ciebie uśmiecha. (Marek Aureliusz) ",

        "Ars longa, vita brevis – sztuka długa, życie krótkie. (Hipokrates)",

        "Przeszłość organizuje się wciąż na nowo wraz z teraźniejszością. (Jean Paul Sartre)",

        "Co jest najśmieszniejsze w ludziach: Zawsze myślą na odwrót: spieszy im się do dorosłości, a potem wzdychają "
        "za utraconym dzieciństwem. Tracą zdrowie by zdobyć pieniądze, potem tracą pieniądze by odzyskać zdrowie. Z "
        "troską myślą o przyszłości, zapominając o chwili obecnej i w ten sposób nie przeżywają ani teraźniejszości "
        "ani przyszłości. Żyją jakby nigdy nie mieli umrzeć, a umierają, jakby nigdy nie żyli. (Paulo Coelho, "
        "Być jak płynąca rzeka)",

        "Jestem przekonany, że przerażający upadek moralności, jakiego jesteśmy świadkami w dzisiejszych czasach, "
        "jest rezultatem mechanizacji i dehumanizacji naszego życia – zgubnych produktów ubocznych mentalności "
        "naukowo – technicznej. (Albert Einstein)",

        "Przyszłość będzie szczodra jedynie wtedy, kiedy wszystko ofiarujesz teraźniejszości. (Albert Camus)",

        "Ludzie ludziom zgotowali ten los. (Zofia Nałkowska, Medaliony)",

        "Przyszłość zależy od tego, co robimy w teraźniejszości. (Mahatma Gandhi)",

        "Jeśli nie umiesz latać, biegnij. Jeśli nie umiesz biegać, chodź. Jeśli nie umiesz chodzić, czołgaj się. Ale "
        "bez względu na wszystko – posuwaj się naprzód. (M.L. King)",

        "Najlepszy moment, aby posadzić drzewo był 20 lat temu. Drugi najlepszy moment jest teraz. (Przysłowie "
        "chińskie)",

        "Mogę zaakceptować porażkę, ale nie mogę zaakceptować braku próby. (Michael Jordan)",

        "– Jaki dziś dzień? – zapytał Puchatek. "
        "– Dziś – odpowiedział Prosiaczek. "
        "Na to Puchatek: – To mój ulubiony dzień. (A.A. Milne, Kubuś Puchatek)",

        "Nie proszę o cuda czy wizje, ale o siłę, by stawić czoła codzienności. (Antoine de Saint-Exupéry)",

    ]
    day_thought = random.choice(THOUGHT_LIST)
    return render(request, 'thought.html', context={'day_thought': day_thought})
