echo "generating tank consumtion..."
python3 gen/gen_tank_consumption.py
echo "generating tank info..."
python3 gen/gen_tank_info.py
echo "pushing data in database..."
python3 gen/put_datas_in_db.py