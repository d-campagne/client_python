Report for Assignment 1 resit


Project chosen


Name: Client_python

URL: https://github.com/prometheus/client_python

Number of lines of code and the tool used to count it: 

Lines: 7428 

Tool used: lizard

Programming language: Python


Coverage measurement with existing tool

To meassure the original coverage of the code I used coverage which I ran with the command: 

coverage run -m pytest, while I was already in the tests directory

![Screenshot 2024-07-10 041002](https://github.com/d-campagne/client_python/assets/121505924/6c7d4ab3-bbde-4d58-afd3-44ae041fe011)


Coverage improvement 

Individual tests 

Function 1: _bake_output()

https://github.com/prometheus/client_python/commit/629f4b3f368c984f4567045dfa7520e39ccca6bc

Old coverage:

![Screenshot 2024-07-08 180642](https://github.com/d-campagne/client_python/assets/121505924/12fb6778-70ca-472c-ba29-f4c08f5193dd)

New coverage:

![Screenshot 2024-07-10 021559](https://github.com/d-campagne/client_python/assets/121505924/2d9552d8-9737-4817-89d5-7dc5df201c2d)

Improved coverage:

![Screenshot 2024-07-10 022422](https://github.com/d-campagne/client_python/assets/121505924/5aa30a14-fb6b-45fb-a72a-d7244f4e90fb)

The old coverage was 2/3, because only 2 branches were hit of the 3 branches. I improved this coverage to 100% especially by adding tests for the first if statement, but also not forgetting to create tests for the second if statement, in order for every branch to be hit

Function 2: write_to_textfile()

https://github.com/prometheus/client_python/commit/629f4b3f368c984f4567045dfa7520e39ccca6bc

Old coverage:

![Screenshot 2024-07-08 181208](https://github.com/d-campagne/client_python/assets/121505924/ce59427a-b1e1-4299-bc75-daf18e5ac4c8)

New coverage:

![Screenshot 2024-07-10 021718](https://github.com/d-campagne/client_python/assets/121505924/f0913404-b9d7-42b4-9d3b-006efe69f4e1)

![Screenshot 2024-07-10 022457](https://github.com/d-campagne/client_python/assets/121505924/4cb5f675-3a0b-4021-b908-500aacb0052b)

The old coverage was 0%, because none of the branches were hit. I improved the coverage to 100% by adding tests that hit every branch


Overall 

Old coverage:

![Screenshot 2024-07-10 041002](https://github.com/d-campagne/client_python/assets/121505924/7bf5f2dd-31bc-427e-854e-bd9de022acac)

New coverage:

![Screenshot 2024-07-10 041015](https://github.com/d-campagne/client_python/assets/121505924/8e99d10d-8e0a-4273-b03d-2a1c7ea4e553)
