# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import gridworld

import random,util,math
import copy

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        #initialize q-values in dictionary
        self.qValues = {}

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        # check if state is in the dictionary
        # check if action is in the
        if (state in self.qValues) and (action in self.qValues[state]):
            return self.qValues[state][action]
        return 0.0

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        # function to map
        def qFuntion(action):
            # print("MAP", state, action)
            return self.getQValue(state, action)

        # map each legal action to qValue
        qMap = map(qFuntion, self.getLegalActions(state))
        # print("QMAP", max(map(qFunction, self.getLegalActions(state)), default=0.0))

        return max(qMap, default=0.0)

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        # function to map
        def qFunction(action):
            # print("MAP", state, action)
            return self.getQValue(state, action)

        # get correct action from legal actions
        maxAction = max(self.getLegalActions(state), key=qFunction, default=None)

        # return max(self.getLegalActions(state), key=qFunction, default=None)
        return maxAction

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = self.computeActionFromQValues(state)
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        #flip coin = boolean (true or false)
        # print(util.flipCoin(1 - self.epsilon), self.epsilon)
        if util.flipCoin(1 - self.epsilon):
            #if true return computed action from qValues
            return action
        #if false randomize the returned action
        return random.choice(legalActions)

    def update(self, state, action, nextState, reward: float):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        # print(self.qValues)
        # print(self.getValue(state), self.getValue(nextState))
        # print(self.getQValue(state, action), self.getQValue(nextState, action))

        # if state is not in the dictionary set then set it to 0.0
        if state not in self.qValues:
            self.qValues[state] = {action: 0.0}

        # formula
        # (1-a)(Q(s)) + a (r(s, a, s') + gamma(V(s')))
        self.qValues[state][action] = (1 - self.alpha) * self.getQValue(
            state, action) + self.alpha * (reward + self.discount * self.getValue(nextState))

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self, state)
        self.doAction(state, action)
        return action

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent
       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    """Method overloading"""
    def getWeights(self):
        return self.weights

    def getWeight(self, feature):
        # get weights
        weights = self.getWeights()

        # if feature is not in weight dectionary
        if feature not in weights:
            # we set it to 0
            weights[feature] = 0.0

        return weights[feature]

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        # extract features
        features = self.featExtractor.getFeatures(state, action)

        # return sum(features[f] * self.getWeight(f) for f in features)

        qVal = 0
        for each in features:
            qVal += (features[each] * self.getWeight(each))
        return qVal

    def update(self, state, action, nextState, reward: float):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()

        # extract features (w1f1 + w2f2)
        features = self.featExtractor.getFeatures(state, action)

        # formula
        # [r(s, a, s') + gamma(V*(s'))] - Q(s, a)
        difference = (reward + self.discount * self.getValue(nextState)) - self.getQValue(state, action)

        # update new weights
        for each in self.weights:
            # formula wDot' = wDot_n + alpha[difference](fDot_n)
            self.weights[each] += self.alpha * difference * features[each]

    def final(self, state):
        """Called at the end of each game."""
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            # pass

            if self.episodesSoFar == self.numTraining:
                # you might want to print your weights here for debugging
                for weight in self.weights.keys():
                    "Weight: %s; Value %2.2f" % (str(weight), float(self.weights[weight]))
                pass