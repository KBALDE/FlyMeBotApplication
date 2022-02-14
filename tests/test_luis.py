
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from config import DefaultConfig

CONFIG = DefaultConfig()


def test_luis_intent():
    """Check LUIS non-regression on *Top intent*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    #request ='book a flight from Tunis to Toronto between 22 October 2021 to 5 November 2021, for a budget of $3500'
    request = "Travel to Paris"
    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)

    check_top_intent = 'BookFlight'
    is_top_intent = response.top_scoring_intent.intent
    #print(" Intent ? ",  is_top_intent)
    assert check_top_intent == is_top_intent
    print("Intent is checked ", is_top_intent)


def test_luis_origin():
    """Check LUIS non-regression on *Origin*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    #request ='book a flight from Paris to NY between 22 October 2021 to 5 November 2021, for a budget of $3500'
    request = "Traveling from Paris"

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_origin = 'Paris'
    all_entities = response.entities
    #print("Entities", all_entities)
    
    for i in range(0, len(all_entities)):
        #print(all_entities[i].type, all_entities[i].entity)
        if all_entities[i].type == 'or_city':
            #print("yes")
            is_origin = all_entities[i].entity.capitalize()
            #print(is_origin)
    
    assert check_origin == is_origin
    print("origin is checked ", is_origin)



def test_luis_destination():
    """Check LUIS non-regression on *Destination*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='from paris to london with 2000'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_destination = 'London'
    all_entities = response.entities
    
    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'dst_city':
            is_destination = all_entities[i].entity.capitalize()

    assert check_destination == is_destination
    print("destination checked ", is_destination)

def test_luis_budget():
    """Check LUIS non-regression on *Destination*
    """
    # Instantiate prediction client
    clientRuntime = LUISRuntimeClient(
        CONFIG.LUIS_API_HOST_NAME,
        CognitiveServicesCredentials(CONFIG.LUIS_API_KEY))
    
    # Create request
    request ='from paris to london with 2000'

    # Get response
    response = clientRuntime.prediction.resolve(CONFIG.LUIS_APP_ID, query=request)
    
    check_budget = '2000'
    all_entities = response.entities
    
    for i in range(0, len(all_entities)):
        if all_entities[i].type == 'budget':
            is_budget = all_entities[i].entity

    assert check_budget == is_budget
    print("Budget checked ", is_budget)




if __name__=="__main__":

    test_luis_intent()
    test_luis_origin()
    test_luis_destination()
    test_luis_budget()
    
    #assert check_destination == is_destination