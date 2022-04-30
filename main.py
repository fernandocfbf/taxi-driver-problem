from classes.MeuTaxi import MeuTaxi

import gym

env = gym.make("Taxi-v3").env
state = env.reset()
env.render()
taxi = MeuTaxi(env.desc, env.decode(state))
taxi.path()
for step in taxi.path():
    state, reward, done, info = env.step(step)
    env.render()
if done:
    print("Soube encontrar a solucao correta")
else:
    print("Algo deu errado!")