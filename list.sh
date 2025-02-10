gitignorefiles=$(cat .gitignore)
excludedfiles=$(cat .excluded)

text="$gitignorefiles $excludedfiles"

delimiter=$'\n'

string=$text$delimiter

declare -a newarray
while [[ $string ]]; do
 newarray+=( "${string%%"$delimiter"*}" )
 string=${string#*"$delimiter"}
done

command="find . -mindepth 1 -maxdepth 1"

IFS=$'\n'
for value in ${newarray[@]}
do
  val=$(printf "! -name \"%s" $value)
  if [[ "${val: -1}" == "/" ]]; then
    val=$(echo "$val" | sed 's/.$//')
  fi
  command="$command $val\""
done

echo "$command"
mkdir -p docs/
IFS=$'\n'
for item in $(eval $command); do
  cp -r "$item" docs/
done