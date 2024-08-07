#!/usr/bin/env sh

tooltip=$(swaymsg -r -t get_tree | jq -r 'recurse(.nodes[]) | first(select(.name=="__i3_scratch")) | .floating_nodes | .[] | "\(.app_id) | \(.name)"')
count=$(printf "%s" "$tooltip" | grep -c '^')

# I want to know what in it right , just do some thing for me, build a json string
if [ "$count" -eq 0 ]; then
    exit 1
elif [ "$count" -eq 1 ]; then
    class="one"
elif [ "$count" -eq 2 ]; then
    class="two"
elif [ "$count" -gt 1 ]; then
    class="many"
else
    class="unknown"
fi

printf '{"text":"%s", "class":"%s", "alt":"%s", "tooltip":"%s"}\n' "$count" "$class" "$class" "$(echo "${tooltip}" | sed -z 's/\n/\\n/g')"
