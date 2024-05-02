#include <iostream>
#include "NetConfig/kmboxNet.h"
#include "NetConfig/HidTable.h"
#include <windows.h>

// Hàm để theo dõi sự kiện chuột
LRESULT CALLBACK MouseHookProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0) {
        if (wParam == WM_MOUSEMOVE) {
            // Lấy thông tin về tọa độ chuột
            MSLLHOOKSTRUCT *hookStruct = (MSLLHOOKSTRUCT *)lParam;
            int x = hookStruct->pt.x;
            int y = hookStruct->pt.y;
            // Gọi hàm để gửi tọa độ chuột đến thiết bị kmbox
            kmNet_mouse_move(x, y);
        }
    }
    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

// Hàm để theo dõi sự kiện nhấn phím
LRESULT CALLBACK KeyboardHookProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode >= 0) {
        if (wParam == WM_KEYDOWN || wParam == WM_KEYUP) {
            // Lấy thông tin về mã phím
            KBDLLHOOKSTRUCT *hookStruct = (KBDLLHOOKSTRUCT *)lParam;
            int vkKey = hookStruct->vkCode;
            // Gọi hàm để gửi mã phím đến thiết bị kmbox
            if (wParam == WM_KEYDOWN) {
                kmNet_keydown(vkKey);
            } else {
                kmNet_keyup(vkKey);
            }
        }
    }
    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int main()
{
    // Kết nối đến thiết bị kmbox
    int ret = kmNet_init((char*)"192.168.2.188", (char*)"16582", (char*)"75C65054"); // Thay thế bằng địa chỉ IP, cổng và địa chỉ MAC thực tế của thiết bị

    // Thiết lập hook cho sự kiện chuột
    HHOOK mouseHook = SetWindowsHookEx(WH_MOUSE_LL, MouseHookProc, NULL, 0);
    // Thiết lập hook cho sự kiện phím
    HHOOK keyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardHookProc, NULL, 0);

    // Vòng lặp chính
    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Giải phóng hook khi kết thúc chương trình
    UnhookWindowsHookEx(mouseHook);
    UnhookWindowsHookEx(keyboardHook);

    return 0;
}
