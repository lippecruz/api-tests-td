echo "*********************************************"
echo "*************** RUNNING TESTS ***************"
echo "*********************************************"

echo "=============== GET METHOD =================="
pytest specs/get-spec.py

echo "=============== POST METHOD ================="
pytest specs/post-spec.py

echo "============== DELETE METHOD ================"
pytest specs/delete-spec.py

echo "================ PUT METHOD ================="
pytest specs/put-spec.py

echo "*********************************************"
echo "*********** FINISIH RUNNING TESTS ***********"
echo "*********************************************"