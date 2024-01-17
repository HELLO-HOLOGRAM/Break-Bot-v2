import asyncio

from org.breaktheheli.net.net_client import AllConnector


async def tester():
    text = 'http://wq.sys-all.cn/qrcode/req/MAID240117220353BCA0CA6C79B28A70B564C9CB4206F996896CA583590860ED0F90051D93F43770.html?l=1705500833&t=E8889EE8908C4458202F20E4B8ADE4BA8CE88A82E5A58F20E799BBE585A5E4BA8CE7BBB4E7A081&d=E68A8AE4B88BE696B9E4BA8CE7BBB4E7A081E5AFB9E58786E69CBAE58FB0E689ABE68F8FE5A484EFBC8CE58FAFE794A8E69CBAE58FB0E69C89E38090E8889EE8908C4458E38091E5928CE38090E4B8ADE4BA8CE88A82E5A58FE38091'
    conn = AllConnector()
    await conn.get_uid(text)
    print(conn.payload)
    pass


if __name__ == '__main__':
    asyncio.run(tester())