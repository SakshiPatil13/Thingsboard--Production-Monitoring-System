import random  # import random to genrate random machine data
import time    # import time to specify data upload interval
import requests  # Import requests library to send requests to Thingworx

url1 = 'http://demo.thingsboard.io:80/api/v1/vlv4JY1RKzfxxvxwcWFr/telemetry'
url2 = 'http://demo.thingsboard.io:80/api/v1/l8LA9KnFLG6fd8NLw4NX/telemetry'
url3 = 'http://demo.thingsboard.io:80/api/v1/G7I9ti7lOwLH9TSZAvbw/telemetry'
# Specify the thingsboard url

headers = {
    'Content-Type': 'application/json'
}

# pieces = [0]
# running_status = [0]
running1 = [0]
avg_ct1 = 0
running3 = [0]
avg_ct3 = 0
running2 = [0]
avg_ct2 = 0
pieces1 = [0]
stops1 = [0]
downtime1 = [0]
pieces2 = [0]
stops2 = [0]
downtime2 = [0]
pieces3 = [0]
stops2 = [0]
downtime3 = [0]
component1 = [0]


def thingsboard_upload1(machine, machine_description, component, component_description, running, status, avg_ct, pieces, stops, downtime):
    data = {'Machine Number': machine, 'Machine Description': machine_description,
            'Component Number': component, 'Component Description': component_description,
            'Running Status': running, 'Status': status, "Avg. Cycle Time": avg_ct,
            "Pieces": pieces, "Stops": stops, "Downtime": downtime}
    response = requests.post(url1, headers=headers, json=data)
    print 'Machine1 Response Code:', response.status_code
    print "\n"


def thingsboard_upload2(machine, machine_description, component, component_description, running, status, avg_ct, pieces, stops, downtime):
    data = {'Machine Number': machine, 'Machine Description': machine_description,
            'Component Number': component, 'Component Description': component_description,
            'Running Status': running, 'Status': status, "Avg. Cycle Time": avg_ct,
            "Pieces": pieces, "Stops": stops, "Downtime": downtime}
    response = requests.post(url2, headers=headers, json=data)
    print 'Machine2 Response Code:', response.status_code
    print "\n"


def thingsboard_upload3(machine, machine_description, component, component_description, running, status, avg_ct, pieces, stops, downtime):
    data = {'Machine Number': machine, 'Machine Description': machine_description,
            'Component Number': component, 'Component Description': component_description,
            'Running Status': running, 'Status': status, "Avg. Cycle Time": avg_ct,
            "Pieces": pieces, "Stops": stops, "Downtime": downtime}
    response = requests.post(url3, headers=headers, json=data)
    print 'Machine2 Response Code:', response.status_code
    print "\n"


while True:
    machine1 = 1
    print "Machine Number1: ", machine1
    machine_description1 = "Machine 1"
    print "Machine Description1: ", machine_description1
    component1 = random.sample(range(1, 8), 1)
    print "Component Number1: ", component1[0]
    component_description1 = "Component " + str(component1[0])
    print "Component Description1: ", component_description1
    running1 = random.sample(range(0, 2), 1)
    print "Running Status1", running1[0]
    if running1[0] == 1:
        status1 = "ON"
        print "Status1: ", status1
        avg_ct1 = 6
        print "Avg. Cycle Time1: ", avg_ct1
        pieces1 = random.sample(range(1, 24), 1)
        print "Pieces1: ", pieces1[0]
        stops1 = random.sample(range(1, 8), 1)
        print "Stops1: ", stops1[0]
        downtime1 = random.sample(range(0, 1), 1)
        print "Downtime1: ", downtime1

    else:
        status1 = "OFF"
        print "Status1: ", status1
        avg_ct1 = 0
        print "Avg. Cycle Time1: ", avg_ct1
        pieces1 = random.sample(range(0, 1), 1)
        print 'Pieces1: ', pieces1
        stops1 = random.sample(range(0, 1), 1)
        print "Stops1: ", stops1
        downtime1 = random.sample(range(1, 8), 1)
        print "Downtime1: ", downtime1[0]
    thingsboard_upload1(machine1, machine_description1,  component1[0], component_description1, running1[0], status1, avg_ct1, pieces1[
                        0], stops1[0], downtime1[0])

    machine2 = 2
    print "Machine Number2: ", machine2
    machine_description2 = "Machine 2"
    print "Machine Description2: ", machine_description2
    component2 = random.sample(range(1, 8), 1)
    print "Component Number2: ", component2[0]
    component_description2 = "Component " + str(component2[0])
    print "Component Description2: ", component_description2
    running2 = random.sample(range(0, 2), 1)
    print "Running Status2", running2[0]
    if running2[0] == 1:
        status2 = "ON"
        print "Status2: ", status2
        avg_ct2 = 12
        print "Avg. Cycle Time2: ", avg_ct2
        pieces2 = random.sample(range(1, 18), 1)
        print "Pieces2: ", pieces2[0]
        stops2 = random.sample(range(1, 8), 1)
        print "Stops2: ", stops2[0]
        downtime2 = random.sample(range(0, 1), 1)
        print "Downtime2: ", downtime2

    else:
        status2 = "OFF"
        print "Status2: ", status2
        avg_ct2 = 0
        print "Avg. Cycle Time2: ", avg_ct2
        pieces2 = random.sample(range(0, 1), 1)
        print 'Pieces2: ', pieces2
        stops2 = random.sample(range(0, 1), 1)
        print "Stops2: ", stops2
        downtime2 = random.sample(range(1, 8), 1)
        print "Downtime2: ", downtime2[0]
    thingsboard_upload2(machine2, machine_description2, component2[0], component_description2, running2[0], status2, avg_ct2, pieces2[
                        0], stops2[0], downtime2[0])

    machine3 = 3
    print "Machine Number3: ", machine3
    machine_description3 = "Machine 3"
    print "Machine Description3: ", machine_description3
    component3 = random.sample(range(1, 8), 1)
    print "Component Number3: ", component3[0]
    component_description3 = "Component " + str(component3[0])
    print "Component Description3: ", component_description3
    running3 = random.sample(range(0, 2), 1)
    print "Running Status3", running3[0]
    if running3[0] == 1:
        status3 = "ON"
        print "Status3: ", status3
        avg_ct3 = 60
        print "Avg. Cycle Time3: ", avg_ct3
        pieces3 = random.sample(range(1, 9), 1)
        print "Pieces3: ", pieces3[0]
        stops3 = random.sample(range(1, 8), 1)
        print "Stops3: ", stops3[0]
        downtime3 = random.sample(range(0, 1), 1)
        print "Downtime3: ", downtime3

    else:
        status3 = "OFF"
        print "Status3: ", status3
        avg_ct3 = 0
        print "Avg. Cycle Time3: ", avg_ct3
        pieces3 = random.sample(range(0, 1), 1)
        print 'Pieces3: ', pieces3
        stops3 = random.sample(range(0, 1), 1)
        print "Stops3: ", stops3
        downtime3 = random.sample(range(1, 8), 1)
        print "Downtime3: ", downtime3[0]
    thingsboard_upload3(machine3, machine_description3, component3[0], component_description3, running3[0], status3, avg_ct3, pieces3[
                        0], stops3[0], downtime3[0])

    time.sleep(5)
