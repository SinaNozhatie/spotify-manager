// اضافه کردن تاییدیه برای حذف عضو
function confirmDelete(memberName) {
    return confirm(`Are you sure you want to remove ${memberName}?`);
}

// بررسی تاریخ‌های ورودی
document.addEventListener('DOMContentLoaded', function() {
    const startDate = document.getElementById('id_start_date');
    const endDate = document.getElementById('id_end_date');

    if(startDate && endDate) {
        endDate.addEventListener('change', function() {
            if(startDate.value > endDate.value) {
                alert('End date cannot be before start date!');
                endDate.value = '';
            }
        });
    }
});

// نمایش ظرفیت باقیمانده به صورت پویا
function updateAvailableSlots(accountId) {
    fetch(`/api/account/${accountId}/slots/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('available-slots').textContent = data.available_slots;
        });
}
