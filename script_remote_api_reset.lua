function sysCall_init()
    sim = require('sim')
    simRemoteApi.start(19997)
    simRemoteApi.start(19998)
    -- do some initialization here
end

function sysCall_actuation()
    -- put your actuation code here
end

function sysCall_sensing()
    -- put your sensing code here
end

function sysCall_cleanup()
    -- do some clean-up here
end

-- See the user manual or the available code snippets for additional callback functions and details
