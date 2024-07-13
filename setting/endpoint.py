# (========================== Host ==========================)
import os

host_gorest = "https://gorest.co.in/public/v2"
# inisialisasi host qase diambil dri qase
host_qase_io = "https://api.qase.io/v1"

# (========================== EndPoint ==========================)
api_user = host_gorest + "/users"
api_user_wrong = host_gorest + "/userssss"
# endpoint qase io
api_result_qase_io = host_qase_io + "/result"

# (========================== qase ==========================)
# token qase diambil dri qase dan nanti diakhir disimpan di variable secret github, dan
# saat ditrigger ditangkap oleh kode dibawah :
TOKEN_QASE = os.environ.get('QASE_IO_TOKEN')

# project id dan test run id diambil dri qase
PROJECT_CASE_QASE_IO = "TY"
TEST_RUN_QASE_IO = "1"

# (========================== slack ==========================)
# buat menangkap endpoint webhook slack yang sudah di simpan sebagai github secret
WEBHOOK = os.environ.get('WEBHOOK_SLACK')

# (========================== netliify ==========================)
# menangkap endpoint output netlify deployment
URL_NETLIFY = os.environ.get('URL_NETLIFY')