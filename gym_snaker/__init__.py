from gym.envs.registration import register

register(
    id='snaker-v0',
    entry_point='gym_snaker.envs:SnakerEnv',
)
register(
    id='snaker-extrahard-v0',
    entry_point='gym_snaker.envs:SnakerExtraHardEnv',
)
