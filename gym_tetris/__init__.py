"""Registration code of Gym environments in this package."""
import math
import gym
from .tetris_env import TetrisEnv


gym.envs.registration.register(
    id='Tetris-v0',
    entry_point='gym_tetris:TetrisEnv',
    max_episode_steps=9999999,
    reward_threshold=32000,
    kwargs={'max_steps': math.inf},
    nondeterministic=True,
)


def make(environment: str) -> gym.Env:
    """Make the environment and return it. same as `gym.make`."""
    return gym.make(environment)


# define the outward facing API of this module (none, gym provides the API)
__all__ = [
    TetrisEnv.__name__,
    make.__name__,
]
