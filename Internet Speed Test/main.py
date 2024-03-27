import speedtest


def internet_speed_test():
    test = speedtest.Speedtest()
    download_speed = test.download()/(1024*1024*8)
    upload_speed = test.upload()/(1024*1024*8)
    ping = test.results.ping
    print(f'your download speed: {download_speed:.2f} MBps')
    print(f'your upload speed: {upload_speed:.2f} MBps')
    print(f'your ping time: {ping:.2f} ms')

if __name__ == '__main__':
    print('Internet Speed Test running....')
    internet_speed_test()

