import io, datetime

states = {
    0 : "info  ",
    1 : "warn  ",
    2 : "error ",
    3 : "accept",
    4 : "deny  "
}

def log(mesgType, message):

    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    mesgType = states[mesgType] if type(mesgType) == int else mesgType

    tolog = "@%s(UTC) : %s : \'%s\'\n" % (timestamp, mesgType, message)

    with open("serverLog.log", 'a') as log:
        log.write(tolog)
