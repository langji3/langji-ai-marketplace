# Apifox 录入清单

## 公共信息

| 项目 | 内容 |
| --- | --- |
| 来源 | 需求 / Spec / Diff / 实现摘要 / 交付摘要 |
| 模式 | Apifox Entry Catalog / Apifox CLI Sync Plan |
| Apifox Project | 只填写非敏感的 projectId / 不适用 |
| 模块 |  |
| Apifox Branch | AI 分支名 / 只读不适用 / 待确认 |
| 逻辑业务目录 | 由 AI 按接口职责推导，待用户确认 |
| 接口目录 | 只读建议 / 已解析目录 ID / 待确认 |
| 响应模型目录 | 只读建议 / 已解析目录 ID / 待确认 |
| Base Path | `/{basePath}` |
| 认证方式 | JWT 登录态 / 无需登录 / 管理端权限 |
| 返回结构 | 以后端实际返回类型为准，例如 `BaseResponse<T>` / `Result<T>` |
| 时间格式 | `yyyy-MM-dd HH:mm:ss` |
| 本次变更类型 | 新增 / 修改 / 删除 / 行为调整 |
| 兼容性 | 兼容 / 不兼容 / 待确认 |

## 一、影响范围清单

### 1. 接口

> 请求侧只在「接口详情」中描述，各接口独立、不共享、不入数据模型库：JSON Body 给 JSON Schema；手工清单模式的 Query 给 Apifox 批量编辑 CSV，CLI 模式直接映射到 endpoint payload；Path / Headers / Cookies 给参数表。响应侧统一进入「响应数据模型库」。

| 变更类型 | Method | Path | 接口名称 | 权限 | 请求参数 | 响应模型 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 新增 / 修改 / 删除 | `GET` | `/example` |  | 登录用户 | Path+Query / Body JSON / 无参数（详见接口详情，内联） | `BaseResponse<ExampleVo>` | 已确认 / 待确认 |

### 2. 响应数据模型库

> 仅收录响应侧数据模型，并保留后端代码中的真实类型名。每个接口实际返回涉及的包装、分页、根对象、嵌套对象和数组元素模型都必须完整列出；模型之间通过 `$ref` 引用时，被引用模型也必须在库中给出完整 schema。枚举字段直接内联在所属响应模型字段内，不单独建枚举模型。

| 变更类型 | 模型名称 | 类型 | 用途 | 被引用来源 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 新增 / 修改 / 删除 | `ExampleVo` | Response |  | `BaseResponseExampleVo` | 已确认 / 待确认 |
| 新增 / 修改 / 删除 | `ExampleItemVo` | Response |  | `ExampleVo.items[]` | 已确认 / 待确认 |
| 新增 / 修改 / 删除 | `PageExampleVo` | Page |  | `BaseResponsePageExampleVo` | 已确认 / 待确认 |

### 3. 权限 / 错误码

| 类型 | 名称 | 变更说明 | 状态 |
| --- | --- | --- | --- |
| 权限 / 错误码 |  |  | 已确认 / 待确认 |

## 二、接口详情

### 1. 接口名称

**变更类型**

```text
新增 / 修改 / 删除 / 行为调整
```

**Method**

```http
GET /example
```

**接口说明**

说明接口用途、业务规则、特殊限制。

**权限**

```text
登录用户
```

**请求参数类型**

```text
Path 参数 / Query 参数 / Body JSON / 无参数
```

> 请求参数在此内联，各接口独立、不共享。Path / Query / Headers / Cookies / Body 均不建立请求数据模型；没有的参数类别直接省略。

**Path 参数（存在时保留）**

| 参数名 | 类型 | 必需 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | `123` | ID |

**Query 参数（存在时保留；手工清单模式使用 Apifox 批量编辑）**

> 手工清单模式使用逗号模式，字段顺序固定为：`参数名,类型,必需,示例值,固定参数值,说明`。每行一个参数；必需使用 `true` / `false`；无固定值时保留空列；含逗号、引号或换行的值遵循标准 CSV 转义。CLI 模式不执行 CSV 导入，而是把同一组参数直接写入经 `cli-schema validate` 校验的 endpoint payload。

```csv
pageNo,integer,false,1,,页码（从1开始）
pageSize,integer,false,20,,每页条数
keyword,string,false,示例关键词,,模糊查询关键词
```

**Headers 参数（存在时保留）**

| 参数名 | 类型 | 必需 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
| `Authorization` | string | 是 | `Bearer <token>` | JWT 登录态请求头 |

**Cookies 参数（存在时保留）**

| 参数名 | 类型 | 必需 | 示例值 | 说明 |
| --- | --- | --- | --- | --- |
|  |  |  |  | 无 Cookie 参数时省略本段 |

**Body JSON Schema（存在 JSON Body 时保留）**

```json
{
  "type": "object",
  "properties": {}
}
```

**响应模型**

```text
BaseResponse<ExampleVo>
```

> 响应不在接口详情中重复 schema，统一引用「响应数据模型库」。这里填写后端实际返回类型；若项目并非 `BaseResponse<ExampleVo>`，应保留代码中的真实包装与模型名。所有传递引用到的响应模型都必须在第三节或第五节完整给出。

**错误场景**

| code | msg | 触发条件 | 状态 |
| --- | --- | --- | --- |
|  |  |  | 已确认 / 待确认 |

**兼容性说明**

-

**Apifox 录入提醒**

- 文档：新增 / 更新 / 删除
- Mock：需要 / 不需要 / 待确认
- 测试用例：正常场景 / 权限失败 / 参数非法 / 业务异常

## 三、响应数据模型库

> 仅收录响应侧数据模型，请求定义不在此处。规则：
>
> 1. 保留后端真实类型名与返回包装，不强制使用 `*Vo` 或 `BaseResponse<T>` 命名。
> 2. 每个接口实际返回涉及的包装、分页、根对象、嵌套对象、继承后会序列化的字段以及数组元素模型都必须完整列出。
> 3. 模型之间通过 `$ref` 互相引用；被引用模型必须一并给出完整 schema，并传递追踪到没有缺失引用为止。
> 4. 枚举型字段直接在所属响应模型字段内用 `enum` + `description` 内联，不单独建立枚举模型。
> 5. 表格说明只能作为补充，不能替代 JSON Schema。

### ExampleVo

> 本接口的响应 VO。`items[]` 通过 `$ref` 引用 `ExampleItemVo`；`status` 为枚举，直接内联。

```json
{
  "type": "object",
  "required": ["id", "status"],
  "properties": {
    "id": {
      "type": "string",
      "description": "ID",
      "example": "123"
    },
    "name": {
      "type": "string",
      "description": "名称",
      "example": "示例"
    },
    "status": {
      "type": "string",
      "description": "状态：PENDING-进行中 / SUCCESS-成功 / FAILED-失败",
      "enum": ["PENDING", "SUCCESS", "FAILED"],
      "example": "PENDING"
    },
    "items": {
      "type": "array",
      "description": "条目列表",
      "items": {
        "$ref": "#/components/schemas/ExampleItemVo"
      }
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "创建时间",
      "example": "2026-07-01 10:00:00"
    }
  }
}
```

### ExampleItemVo

> 被 `ExampleVo.items[]` 引用，按「连带给出」规则在此完整列出。

```json
{
  "type": "object",
  "required": ["itemId"],
  "properties": {
    "itemId": {
      "type": "string",
      "description": "条目 ID",
      "example": "i-001"
    },
    "quantity": {
      "type": "integer",
      "description": "数量",
      "example": 2
    }
  }
}
```

### PageExampleVo

> 分页 VO。`records[]` 通过 `$ref` 引用 `ExampleVo`。

```json
{
  "type": "object",
  "required": ["records", "total"],
  "properties": {
    "records": {
      "type": "array",
      "description": "当前页数据",
      "items": {
        "$ref": "#/components/schemas/ExampleVo"
      }
    },
    "total": {
      "type": "integer",
      "description": "总条数"
    },
    "size": {
      "type": "integer",
      "description": "每页条数"
    },
    "current": {
      "type": "integer",
      "description": "当前页"
    },
    "pages": {
      "type": "integer",
      "description": "总页数"
    }
  }
}
```

## 四、枚举说明

> 枚举值已在所属响应模型字段内以 `enum` 内联；本表仅作补充说明，不单独建枚举模型。

| 所属响应模型 | 字段 | 枚举值 | 含义 | 状态 |
| --- | --- | --- | --- | --- |
| ExampleVo | status | PENDING | 进行中 | 已确认 / 待确认 |
| ExampleVo | status | SUCCESS | 成功 | 已确认 / 待确认 |
| ExampleVo | status | FAILED | 失败 | 已确认 / 待确认 |

## 五、通用响应模型（响应数据模型库的一部分）

### BaseResponseVoid

```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "integer",
      "description": "响应码",
      "example": 200
    },
    "msg": {
      "type": "string",
      "description": "响应消息",
      "example": "操作成功"
    },
    "data": {
      "type": "null",
      "description": "空数据"
    }
  }
}
```

### BaseResponseExampleVo

```json
{
  "type": "object",
  "required": ["code", "msg", "data"],
  "properties": {
    "code": {
      "type": "integer",
      "description": "响应码",
      "example": 200
    },
    "msg": {
      "type": "string",
      "description": "响应消息",
      "example": "操作成功"
    },
    "data": {
      "$ref": "#/components/schemas/ExampleVo"
    }
  }
}
```

### BaseResponsePageExampleVo

```json
{
  "type": "object",
  "required": ["code", "msg", "data"],
  "properties": {
    "code": {
      "type": "integer",
      "description": "响应码",
      "example": 200
    },
    "msg": {
      "type": "string",
      "description": "响应消息",
      "example": "操作成功"
    },
    "data": {
      "$ref": "#/components/schemas/PageExampleVo"
    }
  }
}
```

## 六、待确认项

-

## 七、Apifox 录入结论

- 需要新增接口：
- 需要修改接口：
- 需要删除接口：
- 需要新增 / 修改响应数据模型：
- 需要同步权限说明：是 / 否 / 待确认
- 需要同步错误码：是 / 否 / 待确认
- 需要补充 Mock：是 / 否 / 待确认
- 需要补充测试用例：是 / 否 / 待确认

CLI 同步使用独立的 [操作与恢复记录](cli-operation-plan.md)，本清单不代表外部写入授权。
