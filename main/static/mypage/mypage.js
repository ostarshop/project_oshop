// 오늘 날짜 생성
function getToday() {
    const d = new Date();
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2,'0');
    const day = String(d.getDate()).padStart(2,'0');
    return `${y}-${m}-${day}`;
}

// 상품 데이터
const products = [
    { id: 1, name: "카피바라 꼬리털", status: "판매중"},
    { id: 2, name: "오른손에 흑염룡", status: "품절"},
    { id: 3, name: "득명파 티셔츠", status: "품절"},
    { id: 4, name: "카피바라 머리털", status: "판매중"},
    { id: 5, name: "득명짱 머리털", status: "판매중"}
].map(item => ({
    ...item,
    date: getToday()
}));

// 댓글 데이터
const comments = [
    { id: 1, content: "카피바라 꼬리털", status: "공개"},
    { id: 2, content: "오이시쿠나레 오이시쿠나레 모에모에큥", status: "비공개"},
    { id: 3, content: "카피바라 꼬리털", status: "공개"},
    { id: 4, content: "카피바라 꼬리털", status: "공개"},
    { id: 5, content: "카피바라 꼬리털", status: "비공개"},
].map(item => ({
    ...item,
    date: getToday()
}));

// 상품 테이블 렌더링
function  renderProductTable() {
    const tbody = document.getElementById("productBody");
    if (!tbody) return;

    if (products.length ===0 ) {
        tbody.innerHTML = `<tr><td colspan="4" style="color:#999;text-align:center;padding:30px;">등록된 상품이 없습니다.</td></tr>`;
        return;
    }

    tbody.innerHTML = products.map(p =>`
        <tr>
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>${p.date}</td>
            <td class="${p.status === "판매중" ? "p-status-on" : "p-status-off"}">${p.status}</td>
        </tr>
    `).join('');
}

// 댓글 테이블 렌더링
function renderCommentTable() {
    const tbody = document.getElementById("commentBody");
    if (!tbody) return;

    if (comments.length === 0) {
        tbody.innerHTML = `<tr><td colspan="5" style="color:#999;text-align:center;padding:30px;">등록된 댓글이 없습니다.</td></tr>`;
        return;
    }

    tbody.innerHTML = comments.map(c => `
        <tr>
            <td>${c.id}</td>
            <td class="c-content" title="${c.content}">${c.content}</td>
            <td>${c.date}</td>
            <td class="${c.status === "공개" ? "c-status-on" : "c-status-off"}">${c.status}</td>
            <td>
                <button class="cbtn cbtn-edit" onclick="editComment(${c.id})">수정</button>
                <button class="cbtn cbtn-delete" onclick="deleteComment(${c.id})">삭제</button>
            </td>
        </tr>
    `).join('');
}

// 댓글 수정 / 삭제
function editComment(id) {
    const comment = comments.find(c => c.id === id);
    const newContent = prompt("내용을 수정하세요:", comment.content);
    if (newContent && newContent.trim() !== "") {
        comment.content = newContent;
        renderCommentTable();
    }
}
function deleteComment(id) {
    if (confirm("이 댓글을 삭제하시겠습니까?")) {
        const idx = comments.findIndex(c => c.id === id);
        if (idx !== -1) {
            comments.splice(idx, 1);
            renderCommentTable();
        }
    }
}

// 페이지 로드 시 두 테이블 모두 렌더링
document.addEventListener("DOMContentLoaded", () => {
    renderProductTable();
    renderCommentTable();
});