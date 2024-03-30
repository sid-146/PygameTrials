from utils.body import Body
from utils.simulate import Simulate
import numpy as np
import utils.colors as colors
from utils.logger import console

MASS_MULTIPLIER = pow(10, 14)

b1 = Body(
    positionVector=np.array([[500, 300, 0]]),
    mass=6 * MASS_MULTIPLIER,
    color=colors.white,
)
b1.updateVelocity(np.array([[60, 0, 0]]))
# console.info(f"Body 1 Initialed at pos : x {300} y {500}")
# console.info(f"Body 1 velocity vector : x {30} y {25}")

b2 = Body(
    positionVector=np.array([[600, 200, 0]]),
    mass=6 * MASS_MULTIPLIER,
    color=colors.green2,
)
b2.updateVelocity(np.array([[-60, 0, 0]]))
# console.info(f"Body 2 Initialed at pos : x {800} y {500}")
# console.info(f"Body 2 velocity vector : x {10} y {15}")

b3 = Body(
    positionVector=np.array([[700, 500, 0]]),
    mass=6 * MASS_MULTIPLIER,
    color=colors.blueviolet,
)
b3.updateVelocity(np.array([[60, 0, 0]]))
# console.info(f"Body 3 Initialed at pos : x {500} y {500}")
# console.info(f"Body 3 velocity vector : x {45} y {45}")

sim = Simulate()
sim.initialiseEnv(bodies=[b1, b2, b3])
sim.explore()
