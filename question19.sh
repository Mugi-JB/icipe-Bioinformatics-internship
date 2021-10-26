echo "What's Your Name?"
read name
now=$(date +%k)
if [[ $now -le 10 ]]
then
    greeting="morning"
elif [[ $now -gt 10 ]] && [[ $now -le 17 ]]
then
    greeting="day"
elif [[ $now -gt 17 ]]
then
    greeting="evening"
fi

echo Good $greeting, $name"! It's" now `date +%r` on this day of `date +%B` `date +%e`
