# DesignnTest

## Server's best result
Keys: 10 clients, 3 for 0 and 7 for 1. Each round training on different dataset sample.
local training epoch is 1. Round num = 5. 
Future: Increase round_num, more local epochs, larger sample size, update the base model.

### Output
INFO :      Starting Flower server, config: num_rounds=5, no round_timeout
INFO :      Flower ECE: gRPC server running (5 rounds), SSL is disabled
INFO :      [INIT]
INFO :      Requesting initial parameters from one random client
INFO :      Received initial parameters from one random client
INFO :      Evaluating initial global parameters
INFO :
INFO :      [ROUND 1]
INFO :      configure_fit: strategy sampled 5 clients (out of 5)
INFO :      aggregate_fit: received 5 results and 0 failures
WARNING :   No fit_metrics_aggregation_fn provided
Saving round 1 aggregated weights...
clients weights info:  {}
INFO :      configure_evaluate: strategy sampled 7 clients (out of 7)
INFO :      aggregate_evaluate: received 7 results and 0 failures
WARNING :   No evaluate_metrics_aggregation_fn provided
INFO :
INFO :      [ROUND 2]
INFO :      configure_fit: strategy sampled 10 clients (out of 10)
INFO :      aggregate_fit: received 10 results and 0 failures
Saving round 2 aggregated weights...
clients weights info:  {}
INFO :      configure_evaluate: strategy sampled 10 clients (out of 10)
INFO :      aggregate_evaluate: received 10 results and 0 failures
INFO :      
INFO :      [ROUND 3]
INFO :      configure_fit: strategy sampled 10 clients (out of 10)
INFO :      aggregate_fit: received 10 results and 0 failures
Saving round 3 aggregated weights...
clients weights info:  {}
INFO :      configure_evaluate: strategy sampled 10 clients (out of 10)
INFO :      aggregate_evaluate: received 10 results and 0 failures
INFO :      
INFO :      [ROUND 4]
INFO :      configure_fit: strategy sampled 10 clients (out of 10)
INFO :      aggregate_fit: received 10 results and 0 failures
Saving round 4 aggregated weights...
clients weights info:  {}
INFO :      configure_evaluate: strategy sampled 10 clients (out of 10)
INFO :      aggregate_evaluate: received 10 results and 0 failures
INFO :      
INFO :      [ROUND 5]
INFO :      configure_fit: strategy sampled 10 clients (out of 10)
INFO :      aggregate_fit: received 10 results and 0 failures
Saving round 5 aggregated weights...
clients weights info:  {}
INFO :      configure_evaluate: strategy sampled 10 clients (out of 10)
INFO :      aggregate_evaluate: received 10 results and 0 failures
INFO :      
INFO :      [SUMMARY]
INFO :      Run finished 5 rounds in 22.28s
INFO :      History (loss, distributed):
INFO :          ('\tround 1: 7.458657741546631\n'
INFO :           '\tround 2: 1.9498776197433472\n'
INFO :           '\tround 3: 1.029028058052063\n'
INFO :           '\tround 4: 1.5441820621490479\n'
INFO :           '\tround 5: 0.8425574898719788\n')
INFO :


## Client's result 
INFO :      [RUN 0, ROUND ]
INFO :      Received: get_parameters message 387b5ed8-a13f-4348-90e2-8c3066af8f58
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 93ba0d0d-f57a-4181-9d8f-cf288ab27322
5
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 447538b1-c39b-48fe-b64c-4186bcb1ee0c
(2756, 32, 32, 3)
(2756, 32, 32, 3)
5
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 49b750cf-e81e-46df-a956-0c2956002292
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message e7fc63f0-e37e-4858-9b14-065d672411a7
5
INFO :
INFO :      [RUN 0, ROUND ]
5
INFO :      Received: train message ecd451f7-11d4-4c34-a4d8-626155d213e5
5
Client client5 - Aggregated Weights (last layer):  [0. 0.]
Client client3 - Aggregated Weights (last layer):  [0. 0.]
Client client1 - Aggregated Weights (last layer):  [0. 0.]
Client client0 - Aggregated Weights (last layer):  [0. 0.]
Client client2 - Aggregated Weights (last layer):  [0. 0.]
(2756, 32, 32, 3)
(2756, 32, 32, 3)
Client client3 - Fit history:  {'loss': [0.1403796374797821], 'accuracy': [0.9200000166893005], 'val_loss': [7.5678911209106445], 'val_accuracy': [0.5]}
Client client3 - Weights after training (last layer):  [-0.0080883  0.0080883]
INFO :      Sent reply
Client client5 - Fit history:  {'loss': [0.14367371797561646], 'accuracy': [0.9200000166893005], 
'val_loss': [7.9242448806762695], 'val_accuracy': [0.5]}
Client client5 - Weights after training (last layer):  [-0.00811881  0.00811881]
INFO :      Sent reply
Client client0 - Fit history:  {'loss': [0.13146834075450897], 'accuracy': [0.9200000166893005], 
'val_loss': [7.587187767028809], 'val_accuracy': [0.5]}
Client client0 - Weights after training (last layer):  [-0.00784876  0.00784876]
INFO :      Sent reply
Client client1 - Fit history:  {'loss': [0.13521255552768707], 'accuracy': [0.9200000166893005], 
'val_loss': [7.786315441131592], 'val_accuracy': [0.5]}
Client client1 - Weights after training (last layer):  [-0.00791263  0.00791263]
Client client2 - Fit history:  {'loss': [0.13867934048175812], 'accuracy': [0.9200000166893005], 
'val_loss': [7.540923595428467], 'val_accuracy': [0.5]}
Client client2 - Weights after training (last layer):  [-0.00797817  0.00797817]
INFO :      Sent reply
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message a72a1bab-9a69-4b9f-9272-ef5a3eaf9a13
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 704db01e-9a98-473b-a045-918b42253774
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 8365ea88-5e29-43d9-81de-2191cd94e392
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 2348f039-f293-408a-8882-743b62b8b9f4
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message d11065cf-0b2c-4ae8-af5f-66d387f9fea6
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message c23b2dbc-aa7d-4a45-ab93-14809b0f65b6
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 19523fab-53e3-4ec7-8f1a-d59821ed6fae
Client client5 - Eval accuracy:  0.5
INFO :      Sent reply
Client client2 - Eval accuracy:  0.5
INFO :      Sent reply
Client client1 - Eval accuracy:  0.5
INFO :      Sent reply
Client client0 - Eval accuracy:  0.5
INFO :      Sent reply
Client client3 - Eval accuracy:  0.5
INFO :      Sent reply
(2756, 32, 32, 3)
(2756, 32, 32, 3)
(2756, 32, 32, 3)
(2756, 32, 32, 3)
(2756, 32, 32, 3)
(2756, 32, 32, 3)
Client client6 - Eval accuracy:  0.5
INFO :      Sent reply
Client client4 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 4f4dc879-d31f-45c2-b719-e753b5379e90
1
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 5852bb6a-5a76-4ba8-baa8-090601afb4cc
INFO :
1
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message be6b9381-0841-45d4-bc23-b4ebe4f4513f
1
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 28817402-cb17-4e9d-a872-f9c32cd29bac
Client client5 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
INFO :
Client client6 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
INFO :      [RUN 0, ROUND ]
1
INFO :      Received: train message ae07b2c6-7052-4976-b074-49654d6d544c
1
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 93ffee06-0dc0-4c7a-9b1b-77a4a52c35e8
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 3e0182d4-aae6-4059-90b8-99100850fc42
1
Client client2 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
Client client0 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
1
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 10e09f65-d7ca-4be2-9cc7-5b8e8c571795
1
Client client1 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
Client client7 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 72f55d91-e4f1-4b95-bb26-4aed80591844
1
Client client3 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 87f1c8e6-2085-4471-b9b7-f5469c50506b
1
Client client4 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
Client client8 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
Client client9 - Aggregated Weights (last layer):  [-0.00798932  0.00798932]
Client client1 - Fit history:  {'loss': [6.079654326640593e-07], 'accuracy': [1.0], 'val_loss': [13.085794448852539], 'val_accuracy': [0.5]}
Client client1 - Weights after training (last layer):  [-0.00998824  0.00998824]
Client client0 - Fit history:  {'loss': [8.153861017490271e-07], 'accuracy': [1.0], 'val_loss': [12.874286651611328], 'val_accuracy': [0.5]}
Client client0 - Weights after training (last layer):  [-0.00996779  0.00996779]
INFO :      Sent reply
INFO :      Sent reply
Client client5 - Fit history:  {'loss': [5.161749641047209e-07], 'accuracy': [1.0], 'val_loss': [13.231459617614746], 'val_accuracy': [0.5]}
Client client5 - Weights after training (last layer):  [-0.01006771  0.01006771]
Client client2 - Fit history:  {'loss': [4.2199951622023946e-07], 'accuracy': [1.0], 'val_loss': 
[13.112824440002441], 'val_accuracy': [0.5]}
INFO :      Sent reply
Client client2 - Weights after training (last layer):  [-0.01002014  0.01002014]
INFO :      Sent reply
Client client3 - Fit history:  {'loss': [6.258467237785226e-07], 'accuracy': [1.0], 'val_loss': [13.175536155700684], 'val_accuracy': [0.5]}
Client client3 - Weights after training (last layer):  [-0.01006304  0.01006304]
INFO :      Sent reply
Client client6 - Fit history:  {'loss': [5.030603915656684e-07], 'accuracy': [1.0], 'val_loss': [12.309187889099121], 'val_accuracy': [0.5]}
Client client6 - Weights after training (last layer):  [-0.01150915  0.01148617]
INFO :      Sent reply
Client client4 - Fit history:  {'loss': [3.8027690152375726e-07], 'accuracy': [1.0], 'val_loss': 
[12.122720718383789], 'val_accuracy': [0.5]}
Client client4 - Weights after training (last layer):  [-0.01141024  0.01137018]
INFO :      Sent reply
Client client8 - Fit history:  {'loss': [4.4210615158081055], 'accuracy': [0.03999999910593033], 
'val_loss': [0.6932363510131836], 'val_accuracy': [0.5]}
Client client8 - Weights after training (last layer):  [ 0.00457022 -0.00457022]
INFO :      Sent reply
Client client9 - Fit history:  {'loss': [4.322778224945068], 'accuracy': [0.0], 'val_loss': [0.6932942271232605], 'val_accuracy': [0.5003628730773926]}
Client client9 - Weights after training (last layer):  [ 0.00456975 -0.00456975]
INFO :      Sent reply
Client client7 - Fit history:  {'loss': [4.40605354309082], 'accuracy': [0.03999999910593033], 'val_loss': [0.6932210326194763], 'val_accuracy': [0.5]}
Client client7 - Weights after training (last layer):  [ 0.0045704 -0.0045704]
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 16ed61ce-098a-49b3-8d78-e32e613cab8d
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 663dd05c-9340-4b54-8cbd-b08b2570ce26
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 1599c35c-5a41-4b76-8c91-364ffe80fe48
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 2130c86f-c2ac-46b1-a6f0-40e1ea5c28d2
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 211de925-710a-4b3f-bb81-915cd4e1dbfe
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 7b809939-4ae6-4bbd-ab38-f0dafbb5a107
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 3d73f0d8-4e22-4415-bd66-f5ba72575d35
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message f04c8ffe-f53f-4600-bd33-eaeca96984ac
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message cc490ad5-a2b3-4cde-8715-9b33ab9aa7f5
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 35774b82-12dd-469a-bd60-ff4ba3737679
Client client1 - Eval accuracy:  0.5
INFO :      Sent reply
Client client9 - Eval accuracy:  0.5
INFO :      Sent reply
Client client8 - Eval accuracy:  0.5
INFO :      Sent reply
Client client6 - Eval accuracy:  0.5
INFO :      Sent reply
Client client5 - Eval accuracy:  0.5
Client client3 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :      Sent reply
Client client2 - Eval accuracy:  0.5
INFO :      Sent reply
Client client4 - Eval accuracy:  0.5
INFO :      Sent reply
Client client7 - Eval accuracy:  0.5
INFO :      Sent reply
Client client0 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 979318a1-dced-43b4-b0b0-6e8df2fcfaf9
2
INFO :
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: train message 6aa395b7-fd42-40d0-92f7-c59361fe81cc
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 99484e77-7103-4668-9725-6b1798ed0ceb
2
2
Client client5 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message ab726813-f28a-4441-8948-8488f3ae840a
2
Client client9 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
INFO :
INFO :      [RUN 0, ROUND ]
Client client8 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
INFO :      Received: train message ac0352bb-badd-4ae9-8a3c-6588d7ba4ceb
INFO :
2
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message d8fa70c9-ccc1-42ce-8964-33ea53f1a8ac
INFO :
Client client4 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
INFO :      [RUN 0, ROUND ]
2
INFO :      Received: train message 99035317-3d80-4bf7-aeb4-4e7d0e6296fe
Client client0 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
2
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message f248e325-5b92-4bca-a033-e7c53aea7af0
2
INFO :
Client client7 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 359b04dc-5f6f-47c1-980d-39d4fce80ec9
Client client1 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 2b53e459-e8ed-45de-a849-3fec0ed7991a
2
2
Client client2 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
Client client3 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
Client client6 - Aggregated Weights (last layer):  [-0.00293104  0.00292653]
Client client0 - Fit history:  {'loss': [0.006017033010721207], 'accuracy': [1.0], 'val_loss': [5.77677059173584], 'val_accuracy': [0.5]}
Client client0 - Weights after training (last layer):  [-0.00395337  0.00394887]
Client client8 - Fit history:  {'loss': [1.3756402730941772], 'accuracy': [0.4399999976158142], 'val_loss': [0.7024457454681396], 'val_accuracy': [0.5]}
INFO :      Sent reply
Client client8 - Weights after training (last layer):  [ 0.00860654 -0.00861104]
Client client4 - Fit history:  {'loss': [0.0029684414621442556], 'accuracy': [1.0], 'val_loss': [12.1764497756958], 'val_accuracy': [0.5]}
Client client4 - Weights after training (last layer):  [-0.00835916  0.00835466]
Client client9 - Fit history:  {'loss': [1.367397665977478], 'accuracy': [0.4399999976158142], 'val_loss': [0.7021454572677612], 'val_accuracy': [0.5]}
INFO :      Sent reply
Client client1 - Fit history:  {'loss': [0.0061049372889101505], 'accuracy': [1.0], 'val_loss': [5.1241607666015625], 'val_accuracy': [0.5]}
Client client1 - Weights after training (last layer):  [-0.00395368  0.00394917]
Client client9 - Weights after training (last layer):  [ 0.00861867 -0.00862317]
INFO :      Sent reply
INFO :      Sent reply
Client client5 - Fit history:  {'loss': [0.00631844624876976], 'accuracy': [1.0], 'val_loss': [5.287343978881836], 'val_accuracy': [0.5]}
Client client5 - Weights after training (last layer):  [-0.00398109  0.00397659]
INFO :      Sent reply
INFO :      Sent reply
Client client2 - Fit history:  {'loss': [0.0057250987738370895], 'accuracy': [1.0], 'val_loss': [5.658021450042725], 'val_accuracy': [0.5]}
Client client2 - Weights after training (last layer):  [-0.00393563  0.00393113]
INFO :      Sent reply
Client client3 - Fit history:  {'loss': [0.005711379460990429], 'accuracy': [1.0], 'val_loss': [5.325382709503174], 'val_accuracy': [0.5]}
Client client3 - Weights after training (last layer):  [-0.00394214  0.00393764]
Client client6 - Fit history:  {'loss': [0.003211385104805231], 'accuracy': [1.0], 'val_loss': [12.153376579284668], 'val_accuracy': [0.5]}
Client client6 - Weights after training (last layer):  [-0.00823136  0.00822685]
INFO :      Sent reply
INFO :      Sent reply
Client client7 - Fit history:  {'loss': [1.378758192062378], 'accuracy': [0.4399999976158142], 'val_loss': [0.7022133469581604], 'val_accuracy': [0.5]}
Client client7 - Weights after training (last layer):  [ 0.00860661 -0.00861111]
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message b977b1dd-b5f2-417e-9208-1294c3d72751
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 7808ee7a-449f-4456-b601-ecc6232bb491
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message cc246e52-5275-4b42-b238-455ac6f463ec
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 8b004e3c-dd55-4cbf-9dce-66ef3a7e6d45
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 0e0394d0-da66-46c9-aecd-afffad35c3e2
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 4aa4e440-a32a-4cef-a7c4-307f7ecc12d9
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 22b14011-0ce4-4056-ac54-be63e3c3d694
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 378b82a4-5764-4aae-b4e2-ff25c3337feb
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 647bee76-e7b9-465d-bf9f-05409a7dc3f3
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 50e78482-ff8a-476c-9247-5038b8366d96
Client client0 - Eval accuracy:  0.5
INFO :      Sent reply
Client client8 - Eval accuracy:  0.5
INFO :      Sent reply
Client client1 - Eval accuracy:  0.5
Client client6 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :      Sent reply
Client client7 - Eval accuracy:  0.5
INFO :      Sent reply
Client client3 - Eval accuracy:  0.5
INFO :      Sent reply
Client client5 - Eval accuracy:  0.5
INFO :      Sent reply
Client client2 - Eval accuracy:  0.5
INFO :      Sent reply
Client client4 - Eval accuracy:  0.5
INFO :      Sent reply
Client client9 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message ce15a131-bcc2-4f37-9063-7d798e4b0c10
3
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message abdf8c51-2db1-42f0-9be7-d1c706b8b8c1
3
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message d799d8b4-43cf-4597-a732-894b1f7c7a8c
Client client7 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
INFO :
INFO :      [RUN 0, ROUND ]
3
INFO :      Received: train message 8893f183-3f1b-4a50-b17f-102d3073aaf7
Client client4 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
INFO :
INFO :      [RUN 0, ROUND ]
3
INFO :      Received: train message eb1fad3f-056c-4fe8-a6eb-8625cce91ee8
Client client5 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
3
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message c630505d-1fda-4e43-9401-c19d72705c9d
3
Client client9 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 50d3d30d-dae2-4cc9-adc5-0cb6620c1a34
Client client3 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
3
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 852f7a45-1edc-446e-967b-7ba0fff8dce5
Client client8 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
INFO :
3
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 5e15ca81-c213-4f24-afd7-03f47e30cec1
Client client1 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 33c2c786-7f76-4a19-b541-52a67c82d555
3
3
Client client0 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
Client client6 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
Client client2 - Aggregated Weights (last layer):  [ 0.00170862 -0.00171312]
Client client4 - Fit history:  {'loss': [0.025317084044218063], 'accuracy': [1.0], 'val_loss': [14.37022876739502], 'val_accuracy': [0.5]}
Client client4 - Weights after training (last layer):  [-0.00495066  0.00494615]
INFO :      Sent reply
Client client7 - Fit history:  {'loss': [0.6690284609794617], 'accuracy': [0.6800000071525574], 'val_loss': [0.9727287888526917], 'val_accuracy': [0.5]}
Client client7 - Weights after training (last layer):  [ 0.01167123 -0.01167573]
INFO :      Sent reply
Client client0 - Fit history:  {'loss': [0.027582786977291107], 'accuracy': [1.0], 'val_loss': [9.862256050109863], 'val_accuracy': [0.5]}
Client client0 - Weights after training (last layer):  [-0.00082455  0.00082005]
INFO :      Sent reply
Client client8 - Fit history:  {'loss': [0.6911680698394775], 'accuracy': [0.6800000071525574], 'val_loss': [0.9023352265357971], 'val_accuracy': [0.5]}
Client client8 - Weights after training (last layer):  [ 0.01173946 -0.01174396]
INFO :      Sent reply
Client client5 - Fit history:  {'loss': [0.027835413813591003], 'accuracy': [1.0], 'val_loss': [10.169949531555176], 'val_accuracy': [0.5]}
Client client5 - Weights after training (last layer):  [-0.00075637  0.00075187]
INFO :      Sent reply
Client client9 - Fit history:  {'loss': [0.6664434671401978], 'accuracy': [0.6800000071525574], 'val_loss': [0.9750255346298218], 'val_accuracy': [0.5]}
Client client9 - Weights after training (last layer):  [ 0.01164919 -0.01165369]
INFO :      Sent reply
Client client6 - Fit history:  {'loss': [0.025283824652433395], 'accuracy': [1.0], 'val_loss': [14.143709182739258], 'val_accuracy': [0.5]}
Client client6 - Weights after training (last layer):  [-0.00493853  0.00493402]
INFO :      Sent reply
Client client3 - Fit history:  {'loss': [0.02878892421722412], 'accuracy': [1.0], 'val_loss': [10.181979179382324], 'val_accuracy': [0.5]}
Client client3 - Weights after training (last layer):  [-0.00083975  0.00083525]
INFO :      Sent reply
Client client2 - Fit history:  {'loss': [0.028562437742948532], 'accuracy': [1.0], 'val_loss': [10.281756401062012], 'val_accuracy': [0.5]}
Client client2 - Weights after training (last layer):  [-0.0008242  0.0008197]
INFO :      Sent reply
Client client1 - Fit history:  {'loss': [0.02856970578432083], 'accuracy': [1.0], 'val_loss': [10.04509162902832], 'val_accuracy': [0.5]}
Client client1 - Weights after training (last layer):  [-0.00086269  0.00085818]
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 2c0446d8-15b0-4410-ad62-8ff866c2a35a
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 7746dc42-c876-4326-a675-0004ed208fca
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 92623f98-f358-48b5-b87c-4eef1a7d8fb1
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 88cd0449-0873-49fc-a703-df64175aca66
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 29bdc2d9-e7d2-4378-9d03-dd72495fb634
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 609bac68-16e5-4ef1-8929-9b4ec7a48c69
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 431f07b0-5463-4350-ba9c-ca5bdfbe5425
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 1d67df3a-f918-49a2-87a5-136e4ee33326
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message c049ed7d-b3c9-43c5-84b6-5617fc3759e1
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 2bc25df8-6617-4525-80ad-0456deb41773
Client client0 - Eval accuracy:  0.5
INFO :      Sent reply
Client client6 - Eval accuracy:  0.5
INFO :      Sent reply
Client client3 - Eval accuracy:  0.5
INFO :      Sent reply
Client client8 - Eval accuracy:  0.5
INFO :      Sent reply
Client client1 - Eval accuracy:  0.5
INFO :      Sent reply
Client client2 - Eval accuracy:  0.5
INFO :      Sent reply
Client client7 - Eval accuracy:  0.5
INFO :      Sent reply
Client client5 - Eval accuracy:  0.5
INFO :      Sent reply
Client client4 - Eval accuracy:  0.5
INFO :      Sent reply
Client client9 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message fc4b7d55-70ba-49ce-a18b-85383d245c2e
4
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 8aab16ec-add8-487b-ac74-8ab6d1f58c07
4
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 389ad6c3-43e1-4c00-9610-c6b41586c8de
Client client8 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
4
INFO :
Client client2 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 40cf4d79-c5e9-4f3c-9625-519494518b66
4
Client client6 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 3966148c-8dfa-4496-821d-e593b37f10a8
INFO :
INFO :      [RUN 0, ROUND ]
4
INFO :      Received: train message 515eb36d-ff13-4577-9d04-68e90687a264
Client client9 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
4
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 0dc2b5d1-927f-42de-ad77-ab6908c14375
4
Client client5 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 843e6a26-090f-438a-98a1-d8c3c05618ba
Client client0 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
4
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message b970ea43-9f20-4f00-ae0f-e35edd64ddd5
Client client4 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
INFO :
4
INFO :      [RUN 0, ROUND ]
INFO :      Received: train message 7d227acc-9dfe-4f98-890c-f8a51c1a27c1
4
Client client3 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
Client client1 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
Client client7 - Aggregated Weights (last layer):  [ 0.00484373 -0.00484824]
Client client8 - Fit history:  {'loss': [0.5736169219017029], 'accuracy': [0.7599999904632568], 'val_loss': [2.018498659133911], 'val_accuracy': [0.5]}
Client client6 - Fit history:  {'loss': [0.006424660794436932], 'accuracy': [1.0], 'val_loss': [12.511911392211914], 'val_accuracy': [0.5]}
Client client8 - Weights after training (last layer):  [ 0.01282598 -0.01283049]
Client client6 - Weights after training (last layer):  [ 0.00096886 -0.00097336]
INFO :      Sent reply
INFO :      Sent reply
Client client1 - Fit history:  {'loss': [0.006775549612939358], 'accuracy': [1.0], 'val_loss': [10.018533706665039], 'val_accuracy': [0.5]}
Client client1 - Weights after training (last layer):  [ 0.00339741 -0.00340192]
INFO :      Sent reply
Client client2 - Fit history:  {'loss': [0.0075323451310396194], 'accuracy': [1.0], 'val_loss': [10.435751914978027], 'val_accuracy': [0.5]}
Client client2 - Weights after training (last layer):  [ 0.00334837 -0.00335287]
INFO :      Sent reply
Client client0 - Fit history:  {'loss': [0.007214674726128578], 'accuracy': [1.0], 'val_loss': [10.178955078125], 'val_accuracy': [0.5]}
Client client0 - Weights after training (last layer):  [ 0.00335751 -0.00336202]
INFO :      Sent reply
Client client4 - Fit history:  {'loss': [0.0064478106796741486], 'accuracy': [1.0], 'val_loss': [12.53489875793457], 'val_accuracy': [0.5]}
Client client4 - Weights after training (last layer):  [ 0.00095154 -0.00095604]
Client client3 - Fit history:  {'loss': [0.007498741615563631], 'accuracy': [1.0], 'val_loss': [10.372856140136719], 'val_accuracy': [0.5]}
Client client3 - Weights after training (last layer):  [ 0.00335286 -0.00335736]
INFO :      Sent reply
INFO :      Sent reply
Client client5 - Fit history:  {'loss': [0.007006845436990261], 'accuracy': [1.0], 'val_loss': [10.117012023925781], 'val_accuracy': [0.5]}
Client client5 - Weights after training (last layer):  [ 0.00342722 -0.00343172]
INFO :      Sent reply
Client client7 - Fit history:  {'loss': [0.5725931525230408], 'accuracy': [0.7599999904632568], 'val_loss': [2.015730142593384], 'val_accuracy': [0.5]}
Client client7 - Weights after training (last layer):  [ 0.01267631 -0.01268081]
INFO :      Sent reply
Client client9 - Fit history:  {'loss': [0.5732786059379578], 'accuracy': [0.7599999904632568], 'val_loss': [2.029904842376709], 'val_accuracy': [0.5]}
Client client9 - Weights after training (last layer):  [ 0.01263873 -0.01264323]
INFO :      Sent reply
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 2103506b-a0e4-4f15-b2aa-1aee95d07b10
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 110a64b3-c07f-4815-b0ed-b04c64e683f2
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 1822738b-ce02-4251-841c-618fd1247ef3
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message a5c18fd8-fbc0-4094-b8aa-469b4672631d
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message a8073dbf-f2ed-4a24-b0db-fc3e1dcbc1f9
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 9d79ee6c-ef6f-4114-9a3f-722f5f31b543
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 8642644e-67cd-4e2e-baa5-eb2063141abc
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message 00c4bcd8-c1da-4da8-8979-26efafb2a3ad
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message b434d90c-0233-445b-99c4-61868f79b266
INFO :      
INFO :      [RUN 0, ROUND ]
INFO :      Received: evaluate message f56e630c-ee9b-452b-b9c2-b38848f089f2
Client client8 - Eval accuracy:  0.5
INFO :      Sent reply
Client client7 - Eval accuracy:  0.5
INFO :      Sent reply
Client client9 - Eval accuracy:  0.5
INFO :      Sent reply
Client client4 - Eval accuracy:  0.5
INFO :      Sent reply
Client client1 - Eval accuracy:  0.5
INFO :      Sent reply
Client client2 - Eval accuracy:  0.5
INFO :      Sent reply
Client client3 - Eval accuracy:  0.5
INFO :      Sent reply
Client client5 - Eval accuracy:  0.5
INFO :      Sent reply
Client client6 - Eval accuracy:  0.5
INFO :      Sent reply
Client client0 - Eval accuracy:  0.5
INFO :      Sent reply
INFO :
INFO :      [RUN 0, ROUND ]
INFO :      Received: reconnect message aa498f34-ed84-4f30-bb57-ad0532f89614
INFO :
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: reconnect message c1cb492f-069d-4df4-909e-9a29ecbe6367
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: reconnect message e3fb2412-1739-42bd-87e2-57ef61add2d2
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: reconnect message 84d5599a-14f5-4225-babf-035f4f67c9d6
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: reconnect message 52bd032f-ae2a-4e5b-bb49-1eaaa36cdff7
INFO :      [RUN 0, ROUND ]
INFO :      Received: reconnect message 1005ccf0-9da7-4cfd-bf43-5abcf4166edb
INFO :
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: reconnect message 68c5bd30-c979-4104-a427-55e5bef4439d
INFO :      [RUN 0, ROUND ]
INFO :      Received: reconnect message 9f7a446f-829a-4990-9d24-5e45b894b378
INFO :
INFO :      [RUN 0, ROUND ]
INFO :
INFO :      Received: reconnect message 746b613f-7240-4a88-ac2f-06c5e779678c
INFO :      [RUN 0, ROUND ]
INFO :      Received: reconnect message 4ed0a6ff-4f4e-43ca-a2ad-1920d378315a
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
INFO :      Disconnect and shut down
All scripts have finished executing.