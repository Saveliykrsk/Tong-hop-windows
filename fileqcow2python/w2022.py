import gdown

# URL file Google Drive (thay đổi từ dạng "view" sang "uc" để gdown hoạt động)
url = "https://3zfmbk-my.sharepoint.com/personal/xmbll_3zfmbk_onmicrosoft_com/_layouts/15/download.aspx?UniqueId=78f2fa84-0b8b-4d80-8646-d40b5f1d9fa6&Translate=false&tempauth=v1.eyJzaXRlaWQiOiI2ZmYyZTZkMy1iZmQ0LTRmMDAtYjZkZS0yZDE2NjE1ZTRiYzciLCJhcHBfZGlzcGxheW5hbWUiOiJhbGlzdCIsImFwcGlkIjoiMjIzNTg5MDYtOTI2OS00ZjQzLWIyMzUtMDU3MjU4ZjQ1ZTA0IiwiYXVkIjoiMDAwMDAwMDMtMDAwMC0wZmYxLWNlMDAtMDAwMDAwMDAwMDAwLzN6Zm1iay1teS5zaGFyZXBvaW50LmNvbUAxN2QwODU4Yy04MTliLTQxY2ItODc0My00NDg2ODQyNDViYjIiLCJleHAiOiIxNzM3NDcxNTEyIn0.CgoKBHNuaWQSAjY0EgsIztzTl7eL3T0QBRoOMjAuMTkwLjE0NC4xNzAqLGtHWklGcUhDNVhJM3ZFeVhXc090YVphNlI5cFlmRFd2YWxrSTBrRWZiSTA9MJ4BOAFCEKF5tVOcsABAUldvvWqt0sVKEGhhc2hlZHByb29mdG9rZW5SCFsia21zaSJdcikwaC5mfG1lbWJlcnNoaXB8MTAwMzIwMDI0NzNiMTc4NEBsaXZlLmNvbXoBMoIBEgmMhdAXm4HLQRGHQ0SGhCRbspIBBmJvbGFuZ5oBAmRhogEceG1ibGxAM3pmbWJrLm9ubWljcm9zb2Z0LmNvbaoBEDEwMDMyMDAyNDczQjE3ODSyAQ5hbGxmaWxlcy53cml0ZcgBAQ.TzCM4pFZZ9F9uXOAQW8si_HeXwWMj_9G30wby6Wrex4&ApiVersion=2.0"

# Đường dẫn lưu file sau khi tải
output = "/mnt/a.qcow2"  # Đường dẫn đầy đủ nơi lưu file

# Tải file
gdown.download(url, output, quiet=False)

print(f"File đã được tải về và lưu tại: {output}")
