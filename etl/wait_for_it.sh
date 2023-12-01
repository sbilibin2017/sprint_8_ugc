# WAIT FOR CLICKHOUSE
echo "Start waiting for Clickhouse fully start. Host '$DB_HOST', '$DB_PORT'..."
echo "Waiting for Clickhouse..."
echo "$DB_HOST:$DB_PORT/ping"
while true;
do
  sleep 0.5
  wget --no-verbose --spider http://$DB_HOST:$DB_PORT/ping  
  if [ $? -eq 0 ]
  then    
    exit 0
  fi
done
echo "Clickhouse has started"