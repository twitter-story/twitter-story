from autho import autho

def trends(Trending_in):
    api=autho()


    Jo_trends = api.get_place_trends(23424860)
    Jo_trends_results =[]

    for i in range(5):
        o=Jo_trends[0]["trends"][i]["name"]
        Jo_trends_results.append(o)


    WW_trends = api.get_place_trends(1)
    WW_trends_results =[]

    for i in range(5):
        o=WW_trends[0]["trends"][i]["name"]
        WW_trends_results.append(o)

    return Jo_trends_results,WW_trends_results


    

