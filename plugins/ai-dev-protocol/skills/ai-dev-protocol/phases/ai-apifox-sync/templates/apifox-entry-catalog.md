# Apifox 录入清单

## 公共信息

| 项目 | 内容 |
| --- | --- |
| 来源 | 需求 / Spec / Diff / 实现摘要 / 交付摘要 |
| 模块 |  |
| Base Path | `/{basePath}` |
| 认证方式 | JWT 登录态 / 无需登录 / 管理端权限 |
| 返回结构 | `BaseResponse<T>` |
| 时间格式 | `yyyy-MM-dd HH:mm:ss` |
| 本次变更类型 | 新增 / 修改 / 删除 / 行为调整 |
| 兼容性 | 兼容 / 不兼容 / 待确认 |

## 一、影响范围清单

### 1. 接口

| 变更类型 | Method | Path | 接口名称 | 权限 | 请求 Schemas | 响应模型 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 新增 / 修改 / 删除 | `GET` | `/example` |  | 登录用户 | `ExamplePathParams` / `ExampleQueryParams` / `ExampleHeaders` / `ExampleBody` | `BaseResponse<ExampleVo>` | 已确认 / 待确认 |

### 2. 数据模型

| 变更类型 | 模型名称 | 类型 | 用途 | 状态 |
| --- | --- | --- | --- | --- |
| 新增 / 修改 / 删除 | `ExampleQueryParams` | Request-Path / Request-Query / Request-Header / Request-Cookie / Request-Body / Response / Page / Common / Enum |  | 已确认 / 待确认 |

### 3. 权限 / 错误码 / 枚举

| 类型 | 名称 | 变更说明 | 状态 |
| --- | --- | --- | --- |
| 权限 / 错误码 / 枚举 |  |  | 已确认 / 待确认 |

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

**Path Params Schema**

```json
{
  "type": "object",
  "required": ["id"],
  "properties": {
    "id": {
      "type": "string",
      "description": "ID",
      "example": "123"
    }
  }
}
```

**Query Params Schema**

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

**Headers Schema**

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "Authorization": {
      "type": "string",
      "description": "JWT 登录态请求头，格式为 Bearer token",
      "example": "Bearer <token>"
    }
  }
}
```

**Cookies Schema**

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

**Body JSON 示例**

```json
{}
```

**Body Schema**

```json
{
  "type": "object",
  "properties": {}
}
```

**成功响应示例**

```json
{
  "code": 200,
  "msg": "操作成功",
  "data": {}
}
```

**响应模型**

```text
BaseResponse<ExampleVo>
```

**错误场景**

| code | msg | 触发条件 | 状态 |
| --- | --- | --- | --- |
|  |  |  | 已确认 / 待确认 |

**兼容性说明**

-

**Apifox 录入提醒**

- 文档：新增 / 更新 / 删除
- 示例：需要 / 不需要 / 待确认
- Mock：需要 / 不需要 / 待确认
- 测试用例：正常场景 / 权限失败 / 参数非法 / 业务异常

## 三、数据模型 JSON Schema

> 所有请求模型、响应模型、分页模型、通用响应模型和枚举相关模型都必须给出 JSON Schema。表格说明只能作为补充，不能替代 JSON Schema。

### ExampleBody

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

### ExamplePathParams

```json
{
  "type": "object",
  "required": ["id"],
  "properties": {
    "id": {
      "type": "string",
      "description": "ID",
      "example": "123"
    }
  }
}
```

### ExampleQueryParams

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

### ExampleHeaders

```json
{
  "type": "object",
  "required": [],
  "properties": {
    "Authorization": {
      "type": "string",
      "description": "JWT 登录态请求头，格式为 Bearer token",
      "example": "Bearer <token>"
    }
  }
}
```

### ExampleCookies

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

### ExampleVo

```json
{
  "type": "object",
  "required": [],
  "properties": {}
}
```

### PageExampleVo

```json
{
  "type": "object",
  "required": [],
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

| 字段 | 枚举值 | 含义 | 状态 |
| --- | --- | --- | --- |
| status | 1 | 启用 | 已确认 / 待确认 |

## 五、通用响应模型

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

## 六、待确认项

-

## 七、Apifox 录入结论

- 需要新增接口：
- 需要修改接口：
- 需要删除接口：
- 需要新增 / 修改数据模型：
- 需要同步权限说明：是 / 否 / 待确认
- 需要同步错误码：是 / 否 / 待确认
- 需要补充 Mock：是 / 否 / 待确认
- 需要补充测试用例：是 / 否 / 待确认
