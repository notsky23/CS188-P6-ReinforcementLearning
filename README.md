# CS188-P6-ReinforcementLearning

Disclaimer: This is my attempt at the CS188 coursework 2 from the University of California, Berkeley.<br>

Project Site: https://inst.eecs.berkeley.edu/~cs188/sp22/projects/.<br><br>

## What is this project about?<br>

This project is a practice with different techniques for reinforcement learning agents.<br>

In this project, we will create a PacMan AI agent that uses reinforcement learning algorithms and techniques, and train them for specific objectives (ex. winning the game/getting the highest score).<br>

The agent will start out knowing nothing, but as we train and fine-tune (ex. adapting weights for rewards) the agent, it learns to get better at achieving the desired result.<br><br>

## Results:<br>

You can read more about this module and deliverables at this site: https://inst.eecs.berkeley.edu/~cs188/sp22/project6/<br>

Here are the results I got.<br>

The code is included in this repo.<br><br>

### Warmup with MDP(Markov Decision Process)
![image](https://user-images.githubusercontent.com/98131995/225820562-1663601a-e9ce-44ce-971f-19ce5dd5d97f.png)<br>
![image](https://user-images.githubusercontent.com/98131995/225820651-3f46fe07-fea9-4fd8-baa4-d5c9a88e8b59.png)<br><br>
![Gridworld](https://user-images.githubusercontent.com/98131995/225821743-8408a9b1-7cd0-47ca-8331-98b6ec614c40.gif)<br>
![image](https://user-images.githubusercontent.com/98131995/225821148-2078b6c8-56e8-4c2d-a97b-c4260f9a8e4e.png)<br><br>

### Q1 - Value Iteration<br>
![image](https://user-images.githubusercontent.com/98131995/225824095-dc44c408-c9f9-47ff-9a3c-46f677354d35.png)<br><br>
<img src="https://user-images.githubusercontent.com/98131995/225823541-962e0a37-2eb1-4238-b90e-449f4ff059c3.png" width=50% height=50%><img src="https://user-images.githubusercontent.com/98131995/225823063-b59e39e6-6d87-43bd-9411-614a8cef54f4.png" width=50% height=50%><br>
<img src="https://user-images.githubusercontent.com/98131995/225823586-1c8830ba-c32c-46b3-8dc8-932b229c7008.png" width=50% height=50%><img src="https://user-images.githubusercontent.com/98131995/225823878-678e17ab-ebd8-486c-9116-7525bae39a9c.png" width=50% height=50%><br><br>

### Q2 - Policies<br>
![image](https://user-images.githubusercontent.com/98131995/225827152-8412bec2-a79e-4cc7-b685-de2d4ba9a991.png)<br>
![image](https://user-images.githubusercontent.com/98131995/225827190-ea10f601-f7fb-466c-928d-f94d7c57c8c4.png)<br>
![image](https://user-images.githubusercontent.com/98131995/225827737-4fa8fd4d-5f5f-4db1-9f32-7cf6ea15cae3.png)<br>
<img src="https://user-images.githubusercontent.com/98131995/225829582-184692f1-2ce1-422d-a930-49906db63f93.png" width=50% height=50%><img src="https://user-images.githubusercontent.com/98131995/225829709-b83261a6-0ae0-4c02-a771-dd00c212adaa.png" width=50% height=50%><br>


### Q3 - Q-Learning<br>
![image](https://user-images.githubusercontent.com/98131995/225831054-75f893f9-0bd8-453d-bc90-3eae9b5f0a4c.png)<br>
![image](https://user-images.githubusercontent.com/98131995/225831218-9c9bc99a-d761-4984-a83f-58fd18cf4543.png)<br>
![image](https://user-images.githubusercontent.com/98131995/225831350-3035e5d2-bebc-404e-93ca-28e940d0f557.png)<br><br>

### Q4 - Epsilon Greedy<br>
![image](https://user-images.githubusercontent.com/98131995/225831658-98a4d8db-38a4-4e44-b2f6-32497a64a2b4.png)<br><br>

### Q5 - Q-Learning and Pacman<br>
After 10 training sessions:<br>
![image](https://user-images.githubusercontent.com/98131995/225833590-366f36d2-347e-44dd-a814-ed755c4eb36c.png)<br><br>
After 2000 training sessions:<br>
![image](https://user-images.githubusercontent.com/98131995/225833793-96c1a804-80f3-4fdb-8915-691b30bcbc1c.png)<br><br>

### Q6 - Approximate Q-Learning<br>
![image](https://user-images.githubusercontent.com/98131995/225834168-fc3cad95-78d5-4ba3-999f-b7cd45d17e3a.png)<br>
<img src="https://user-images.githubusercontent.com/98131995/225857647-88cfde9d-d790-40c1-9cf6-89c619a0a635.png" width=50% height=50%><img src="https://user-images.githubusercontent.com/98131995/225857867-f528aa0b-ca2f-4d51-a3cf-bcdd37de9346.png" width=50% height=50%><br>
<img src="https://user-images.githubusercontent.com/98131995/225858011-93c22b52-2637-4e0a-9452-463d497e0487.png" width=50% height=50%><img src="" width=50% height=50%><br><br>
