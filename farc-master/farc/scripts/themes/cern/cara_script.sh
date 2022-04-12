git clone https://gitlab.cern.ch/cara/cara.git
cd farc
git lfs install
git lfs pull
pip install -e .
echo "############################################"
echo "CARA is now running at http://localhost:8080"
echo "############################################"
python -m farc.apps.calculator --theme=farc/apps/templates/cern