import numpy as np
from utils.logger import console


class PhysicsEngine:
    GRAVITATIONAL_CONSTANT = 6.67 * pow(10, -11)
    SCALING_COEFFICIENT = 0.25

    def __init__(self):
        self.bodies: list = None
        self.bodies_position_array: np.array = np.array([]).reshape((0, 3))

    def defineBodies(self, bodies: list[object]):
        # Storing all the bodies in list with an index in an numpy array
        # ? bodies = [[1, body1], [2, body2] ... [n, body_n]]
        self.bodies = [np.array(([i, body])) for i, body in enumerate(bodies)]

    def __calcGravitationalForce(self, m1, m2, dist):
        force = self.GRAVITATIONAL_CONSTANT * m1 * m2 / pow(self.__magnitude(dist) * self.SCALING_COEFFICIENT, 2)
        # force = self.GRAVITATIONAL_CONSTANT * m1 * m2 / pow(self.__magnitude(dist), 2)
        force = force * self.__unitVector(dist)
        return force

    def CalcForce(self):
        distance = []
        forces = []
        netForces = []

        # Calculating distance between two bodies for each body
        for primary in self.bodies:
            console.info(f"Primary {primary[0]}, {primary[1].position}")
            holder = np.array([]).reshape((0, 3))
            for secondary in self.bodies:
                console.info(f"Secondary {secondary[0]}, {secondary[1].position}")
                holder = np.append(
                    holder,
                    (primary[1].position - secondary[1].position)
                    * np.array([[-1, -1, 1]]),
                    axis=0,
                )
                # console.info(f"holder {holder}")
                console.info("---")

            distance.append(holder)
            console.info(f"After iteration : {distance}")

        # Calculating forces between bodies
        for primary in self.bodies:
            pBody = primary[1]
            holder = np.array([]).reshape((0, 3))
            for secondary in self.bodies:
                # for each primary iterating over all the bodies
                sBody = secondary[1]
                # Distance between two bodies
                radius = distance[primary[0]][secondary[0]]
                if self.__magnitude(radius) == 0.0:
                    holder = np.append(holder, np.array([[0.0, 0.0, 0.0]]), axis=0)
                else:
                    force = self.__calcGravitationalForce(
                        pBody.mass, sBody.mass, radius
                    )
                    forceVector = force * np.array([[1, 1, 1]])
                    holder = np.append(holder, forceVector, axis=0)

            forces.append(holder)

        for force in forces:
            netForces.append(force.sum(axis=0))

        return netForces

    @staticmethod
    def __magnitude(arr: list):
        # Distance from center for the 3D vector
        #! d=√x2+y2+z2
        d = np.sqrt(pow(arr[0], 2) + pow(arr[1], 2) + pow(arr[2], 2))
        return d

    def __unitVector(self, arr: list):
        magnitude = self.__magnitude(arr)
        # Representing the actual force on scale of 0 to 1
        unitV = np.array([[arr[0] / magnitude, arr[1] / magnitude, arr[2] / magnitude]])
        return unitV
