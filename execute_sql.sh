if [ "$#" -eq 0 ]; then
	echo "executes sql commands as user 'postgres'"
	echo "usage: script.sh file.sql"
else
	psql -U postgres -a -f $1
fi
