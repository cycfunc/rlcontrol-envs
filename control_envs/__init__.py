from gym.envs.registration import register


# Classic
# ----------------------------------------

register(
    id="control_envs/InvertedCartPole-v0",
    entry_point="control_envs.envs:InvertedCartPoleEnv",
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id="control_envs/InvertedCartPole-v1",
    entry_point="control_envs.envs:InvertedCartPoleEnv",
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id="control_envs/ContinuousCartPole-v0",
    entry_point="control_envs.envs:ContinuousCartPoleEnv",
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id="control_envs/ContinuousCartPole-v1",
    entry_point="control_envs.envs:ContinuousCartPoleEnv",
    max_episode_steps=500,
    reward_threshold=475.0,
)
