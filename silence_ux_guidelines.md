### Silence UX Guidelines

**— Validation Failure as Normal Behavior**

### Core Principle

검증 실패는 오류가 아니다. 검증 실패는 **발화 자격이 없다는 판정**이며, 그 결과는 **침묵**이다.

시스템은 설명하지 않는다. 시스템은 사과하지 않는다. 시스템은 다시 시도하라고 요청하지 않는다.

침묵은 실패 UI가 아니라 **정상 UI**다.

---

### Rendering Rules (Hard Rules)

1. **Validator=false**
   - 화면에 어떤 텍스트도 렌더링하지 않는다.
   - 토스트, 에러 박스, 경고 아이콘 모두 금지.
   - 로그만 남긴다. 사용자는 보지 않는다.

2. **Validator=true + action_permission=handoff**
   - `language_mapping.yaml`에 정의된 **handoff 문장 1개만** 렌더링한다.
   - 추가 설명, 보조 문장, AI 표현 금지.

3. **Validator=true + action_permission≠handoff**
   - Canon이 허용한 단일 판단 문장만 렌더링한다.
   - UI는 판단을 “설명”하지 않는다.

---

### Forbidden UX Patterns

다음은 **절대 금지**된다.

- “모델이 응답하지 않았습니다”
- “AI가 실패했습니다”
- “다시 시도해 주세요”
- 오류 코드, 스택 트레이스, 내부 상태 노출
- 빈 결과에 대한 자동 보완 텍스트

침묵을 **문제처럼 보이게 만드는 모든 시도는 위반**이다.

---

### UI State Matrix

| Canon Result              | UI Output     |
| ------------------------- | ------------- |
| ok=true                   | 단일 판단 문장      |
| ok=false + handoff        | 단일 handoff 문장 |
| ok=false (breach / error) | **침묵**        |
| validator crash           | **침묵**        |

---

### Design Note

사용자가 아무것도 보지 못했다면, 그것은 시스템이 **아무 말도 하지 않기로 결정했기 때문**이다.

침묵은 공백이 아니라 **판단의 경계 표시**다.
