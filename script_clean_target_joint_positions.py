"""
Copyright (C) 2024 Murilo Marques Marinho (www.murilomarinho.info)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>.
"""

"""
This is a particularly useful script for scenes that use set_target_joint_positions. If those
values are sent and the scene is saved, they get stored in a CoppeliaSim buffer that we have
not easy access to. This means that every time the simulation is started, it will move the joints
to the previous target, causing confusion. This script fixes that problem.

However, note that the fact that this changes the values for ALL joints in the scene means that
in some cases this behavior is not welcome. Please adjust as needed.
"""

def sysCall_init():
    sim = require('sim')
    pass

def sysCall_nonSimulation():
    # is executed when simulation is not running
    pass

def sysCall_beforeSimulation():
    """
    We obtain all 'sim.object_joint_type' elements in the scene and, 
    before the simulation starts, set the target joint positions to match
    the current joint positions.
    """
    joints = sim.getObjectsInTree(sim.handle_scene,sim.object_joint_type)
    
    self.done = False
    
    if not self.done:
        for joint in joints:
            sim.setJointTargetPosition(joint, sim.getJointPosition(joint))
        self.done = True


def sysCall_afterSimulation():
    # is executed before a simulation ends
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
