# AIDeer-Streaming

项目仍在施工中，尚未经过测试。

## Introduction

由于流式传输响应需要维护一个长连接，Flask 并不是异步优先的框架，在处理大量长连接并发请求时，性能会受到影响。因此，我们使用了 FastAPI 以实现高性能异步 SSE 服务。

## API Reference

### /tasks/<task_id>/stream

#### GET
获取任务的实时输出。返回为一个 JSON 对象，包含以下字段：

- `status`：任务状态，可能的值为 `running`、`finished`、`failed`。
- `data`：任务输出的数据。当任务状态为 `running` 时，该字段为新增的输出数据；当任务状态为 `finished` 时，该字段为任务的最终输出数据；当任务状态为 `failed` 时，该字段为错误信息。