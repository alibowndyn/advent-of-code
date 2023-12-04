local lines = io.open('../input.txt', 'r'):lines()

local calib_sum = 0


for line in lines do
    if line ~= '' then
        local first = string.match(line,           '%d')
        local last  = string.match(line:reverse(), '%d')

        calib_sum = calib_sum + (first .. last)
    end
end


io.write(calib_sum)