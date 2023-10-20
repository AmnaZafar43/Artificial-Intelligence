import random
GRID_SIZE = 4
grid = [
    ['S', 'F', 'F', 'F'],
    ['F', 'H', 'F', 'H'],
    ['F', 'F', 'F', 'H'],
    ['H', 'F', 'F', 'G']
]

# Discount factor
gamma = 0.9  
# Possible actions
actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']  

# state-value function
V = {}
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        V[(i, j)] = 0.0

# Define the transition probability and rewards
def transition_prob(state, action, next_state):
    i, j = state
    # If in a hole, stay in the hole
    if grid[i][j] == 'H':  
        return 1.0 if state == next_state else 0.0
    # If at the goal, stay at the goal
    if grid[i][j] == 'G':  
        return 1.0 if state == next_state else 0.0
    intended_next_state = get_intended_next_state(state, action)
    if next_state == intended_next_state:
        return 0.7
    else:
        return 0.1

def get_intended_next_state(state, action):
    i, j = state
    if action == 'UP':
        return (max(i - 1, 0), j)
    elif action == 'DOWN':
        return (min(i + 1, GRID_SIZE - 1), j)
    elif action == 'LEFT':
        return (i, max(j - 1, 0))
    elif action == 'RIGHT':
        return (i, min(j + 1, GRID_SIZE - 1))

def reward(state, action):
    i, j = state
    if grid[i][j] == 'H':
        # Negative reward for falling into a hole
        return -1.0  
    elif grid[i][j] == 'G':
        return 1.0 
    else:
        # Small negative reward for other actions
        return -0.1  

# Policy iteration
def policy_iteration():
    policy = {}  
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] not in ('H', 'G'):
                policy[(i, j)] = random.choice(actions)
    while True:
        # Policy evaluation
        while True:
            delta = 0
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    state = (i, j)
                    old_v = V[state]
                    new_v = 0
                    for action in actions:
                        expected_value = 0
                        for next_i in range(GRID_SIZE):
                            for next_j in range(GRID_SIZE):
                                next_state = (next_i, next_j)
                                expected_value += transition_prob(state, action, next_state) * (
                                    reward(state, action) + gamma * V[next_state]
                                )
                                # Equal probability for all actions
                        new_v += 0.25 * expected_value  
                    V[state] = new_v
                    delta = max(delta, abs(new_v - old_v))
            if delta < 1e-6:
                break
        # Policy improvement
        policy_stable = True
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                state = (i, j)
                if grid[i][j] not in ('H', 'G'):
                    old_action = policy[state]
                    action_values = []
                    for action in actions:
                        expected_value = 0
                        for next_i in range(GRID_SIZE):
                            for next_j in range(GRID_SIZE):
                                next_state = (next_i, next_j)
                                expected_value += transition_prob(state, action, next_state) * (
                                    reward(state, action) + gamma * V[next_state]
                                )
                        action_values.append(expected_value)
                    best_action = actions[action_values.index(max(action_values))]
                    policy[state] = best_action
                    if old_action != best_action:
                        policy_stable = False
        if policy_stable:
            break
    return policy

# we solve the problem here and print the optimal policy
optimal_policy = policy_iteration()
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        if grid[i][j] == 'H':
            print('H', end=' ')
        elif grid[i][j] == 'G':
            print('G', end=' ')
        else:
            print(optimal_policy[(i, j)], end=' ')
    print()
