import numpy as np


def PredPrey(prey_birth_rate=0.025, predation_rate=0.0015, predator_efficiency=0.002,
             predator_loss_rate=0.06, initial_prey=50, initial_predators=20, dt=0.25, final_time=365):
    # Initial values
    predators, prey, sim_time = [np.zeros(int(final_time / dt) + 1) for _ in range(3)]

    predators[0] = initial_predators
    prey[0] = initial_prey

    # Calculate the time series
    for t in range(0, sim_time.shape[0] - 1):
        dx = (prey_birth_rate * prey[t]) - (predation_rate * prey[t] * predators[t])
        dy = (predator_efficiency * predators[t] * prey[t]) - (predator_loss_rate * predators[t])

        prey[t + 1] = max(prey[t] + dx * dt, 0)
        predators[t + 1] = max(predators[t] + dy * dt, 0)
        sim_time[t + 1] = (t + 1) * dt

    # Return outcomes
    return {'TIME': sim_time,
            'predators': predators,
            'prey': prey}
