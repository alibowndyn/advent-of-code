local lines = io.open('../input.txt', 'r'):lines()

local num_conversions = {
    ['one']   = 'o1e',
    ['two']   = 't2o',
    ['three'] = 't3e',
    ['four']  = 'f4r',
    ['five']  = 'f5e',
    ['six']   = 's6x',
    ['seven'] = 's7n',
    ['eight'] = 'e8t',
    ['nine']  = 'n9e'
}

local numbers = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
local calib_sum = 0


for line in lines do
    if line ~= '' then
        -- search the line for each number and if there's a match,
        -- use the match as the key in the num_conversions table
        -- and replace the match with the value of that key
        for i = 1, #numbers do
            line = string.gsub(line, numbers[i], num_conversions)
        end


        local first = string.match(line,           '%d')
        local last  = string.match(line:reverse(), '%d')

        calib_sum = calib_sum + (first .. last)
    end
end


io.write(calib_sum)